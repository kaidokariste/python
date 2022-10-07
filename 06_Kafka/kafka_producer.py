from kafka import KafkaProducer
import json
from data import get_registered_user
import time

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers=['<server>:9092'],
                         value_serializer=json_serializer,
                         api_version=(2,0,2))

if __name__ == "__main__":
    while 1 == 1:
        registered_user = get_registered_user()
        print(registered_user)
        # producer.send(<kafka_topic_name)
        producer.send("inimesed", registered_user)
        time.sleep(5)