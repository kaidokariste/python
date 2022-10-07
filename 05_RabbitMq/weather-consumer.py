import pika
import sqlalchemy
from dotenv import load_dotenv
import os
load_dotenv()

"""
Database:
    Define global connection engine.
    Initiated once.
    db_uri = "postgresql://<username>:<PASS>@<HOST>:5432/<DB>"
Rabbit
    rabbit_url "amqp://<rabbit-path>"
    By using amqps:// you will hit certification validation errors, so use amqp:// instead
"""
db_url = os.environ.get("pg_url")
engine = sqlalchemy.create_engine(db_url, pool_size=3, max_overflow=1)
rabbit_url = os.environ.get("rabbit_url")


def pg_connect():
    """
    Connects to Postgres database. Returns connection handler from connection engine.
    Initiated multiple times
    """
    return engine.connect()


def rabbit_connect(rabbit_url):
    """
    Connects to RabbitMq using provided url.
    """
    # Parse connection URL to parameters and create connection to Rabbit
    parameters = pika.URLParameters(rabbit_url)
    connection = pika.BlockingConnection(parameters)
    return connection


def callback(ch, method, properties, body):
    received_message = body.decode()
    print(" [x] %r " % received_message)
    conn = pg_connect()
    conn.execute('INSERT INTO biz.ilmateade(message) VALUES (%s)', received_message)
    conn.close()


def consume_weather_report():

    # Define Rabbit connection instance
    rb_con = rabbit_connect(rabbit_url)
    channel = rb_con.channel()

    # Create a queue
    result = channel.queue_declare(queue='ilm', exclusive=False)

    # Get auomatically queue name from previous statement
    queue_name = result.method.queue
    print('Queue name: ', queue_name)

    # Bind the queue to listen exchange
    channel.queue_bind(exchange='estonia_weather', queue=queue_name, routing_key='ilm')

    print(' [*] Waiting for messages. To exit press CTRL+C')

    # Start consuming messages from our queue
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    consume_weather_report()
