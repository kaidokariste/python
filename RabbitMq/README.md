# Terms and definitions
**Default exchange** allows us to specify exactly to which queue the message should go. Default exchange is identified by an empty string. The queue name needs to be specified in the routing_key parameter  
```channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')```
