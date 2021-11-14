# Terms and definitions
An **exchange** is a very simple thing. On one side it receives messages from producers and the other side it pushes them to queues. The exchange must know exactly what to do with a message it receives.

**Default exchange** allows us to specify exactly to which queue the message should go. Default exchange is identified by an empty string. The queue name needs to be specified in the routing_key parameter  
```channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')```

The core idea in the messaging model in RabbitMQ is that the producer never sends any messages directly to a queue. The messages will be lost if no queue is bound to the exchange yet.      

There are a few exchange types available: 
1. **direct** 
2. **topic** 
3. **headers** 
4. **fanout**.  

The **fanout** exchange is very simple. As you can probably guess from the name, it just broadcasts all the messages it receives to all the queues it knows. Routing key value is ignored as it forwards messages to all known queues.  
Define fanout exchange - ```channel.exchange_declare(exchange='<exchange-name>', exchange_type='fanout')```  
Publish message to exchange - ```channel.basic_publish(exchange='<exchange-name>', routing_key='', body=message)```  
