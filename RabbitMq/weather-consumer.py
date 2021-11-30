import pika
import sqlalchemy

"""
Connects to Postgres database. Returns connection handler.
connection_uri = "postgresql://<username>:<PASS>@<HOST>:5432/<DB>"
"""
connection_uri = ""
engine = sqlalchemy.create_engine(connection_uri)



def callback(ch, method, properties, body):
    print(" [x] %r" % body.decode())
    engine.execute('INSERT INTO ilmateade(message) VALUES (%s)',(body.decode()))


def consume_weather_report():
    # By using amqps:// you will hit certification validation errors, so use amqp:// instead
    url = 'amqp://<amqp-url>'
    parameters = pika.URLParameters(url)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    result = channel.queue_declare(queue='ilm', exclusive=False)
    queue_name = result.method.queue
    print('Queue nimi: ', queue_name)

    channel.queue_bind(exchange='estonia_weather', queue=queue_name, routing_key='ilm')

    print(' [*] Waiting for logs. To exit press CTRL+C')

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

if __name__ == '__main__':
    consume_weather_report()