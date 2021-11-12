from random import randrange
import json
import pika
import time


def ilm():
    towns = ['Tallinn','Tartu','Narva','Valga','Kuressaare']
    random_town= towns[randrange(len(towns))]
    random_temp = randrange(-15,30,1)
    weather_in_town = {"TownName": random_town, "Temperature": random_temp}
    json_weather_in_town = json.dumps(weather_in_town)
    return json_weather_in_town

def send_to_Rabbit():
    weather_forecast = ilm()
    # By using amqps:// you will hit certification validation errors, so use amqp:// instead
    url = 'amqp://<url>'
    parameters = pika.URLParameters(url)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.exchange_declare(exchange='estonia_weather', exchange_type='fanout')

    channel.basic_publish(exchange='estonia_weather',
                          routing_key='',
                          body=weather_forecast)
    print(" [x] Sent " + weather_forecast)
    connection.close()

def messagesender():
    i = 0
    # Send new message after every 5 seconds
    while i < 5:
        send_to_Rabbit()
        i+=1
        print(i)
        time.sleep(1)

if __name__ == "__main__":
    messagesender()
