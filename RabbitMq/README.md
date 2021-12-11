# Terms and definitions
An **exchange** is a very simple thing. On one side it receives messages from producers and the other side it pushes them to queues. The exchange must know exactly what to do with a message it receives.

**Default exchange** allows us to specify exactly to which queue the message should go. Default exchange is identified by an empty string. The queue name needs to be specified in the routing_key parameter  
```channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')```

The core idea in the messaging model in RabbitMQ is that the producer never sends any messages directly to a queue. 

A **binding** is a relationship between an exchange and a queue. The messages will be lost if no queue is bound to the exchange yet.      

There are a few exchange types available: 
1. **direct** 
2. **topic** 
3. **headers** 
4. **fanout**.  

The **fanout** exchange is very simple. As you can probably guess from the name, it just broadcasts all the messages it receives to all the queues it knows. Routing key value is ignored as it forwards messages to all known queues.  
Define fanout exchange - ```channel.exchange_declare(exchange='<exchange-name>', exchange_type='fanout')```  
Publish message to exchange - ```channel.basic_publish(exchange='<exchange-name>', routing_key='', body=message)```  

The **direct exchange** - a message goes to the queues whose binding key exactly matches the routing key of the message. I did example where I posted a message and based on temperature, divided them as summer or winter. So for each message, routing key _season (summer, winter)_ was calculated. Exchange forwarded them to _summer_weather_ or _winter_weather_ queues  
```channel.basic_publish(exchange='estonia_weather', routing_key=season, body=weather_forecast)```
