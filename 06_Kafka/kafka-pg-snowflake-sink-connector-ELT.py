import configparser
import os
import json
import sqlalchemy
from kafka import KafkaConsumer
import pandas as pd
from snowflake.sqlalchemy import URL

# Define empty configuration dictionary
config = {}
g_workdir = os.path.dirname(os.path.realpath(__file__))


def json_serializer(data):
    return json.loads(data.decode('utf-8'))


def read_config():
    """
    Read and parse configuration file
    Add it as key-value pairs in configuration dictionary
    """
    cfg = configparser.ConfigParser()
    cfg.read(g_workdir + '/snowflake.properties.example')
    config.update(cfg['kafka'])
    config.update(cfg['db'])


def snowflake_insert(df, tablename, engine):
    # https://docs.snowflake.com/en/user-guide/sqlalchemy.html#using-the-snowflake-sqlalchemy-toolkit-with-the-python-connector
    con = engine.connect()
    print(df)
    try:
        df.to_sql(tablename, con=engine, index=False, if_exists='append')
    finally:
        con.close()
        engine.dispose()


def kafka_consumer(topic):
    engine = sqlalchemy.create_engine(URL(
        account='se05361.europe-west4.gcp',
        user='user',
        password='pass',
        database='poc',
        schema='stage',
        warehouse='warehouse'
    ))

    consumer = KafkaConsumer(topic,
                             group_id='my-group',
                             bootstrap_servers=['kafka-server:9092'],
                             value_deserializer=json_serializer,
                             auto_offset_reset='earliest',
                             enable_auto_commit=False
                             )
    for message in consumer:
        json_body = json.dumps(message.value)
        d = {'topic': [message.topic], 'offset': [message.offset], 'timestamp': [message.timestamp],'message': [json_body]}
        df = pd.DataFrame(data=d)
        snowflake_insert(df, 'kafka_uci_stage', engine)


if __name__ == '__main__':
    read_config()
    # print(g_workdir)
    print(config)
    kafka_consumer('cyclo.uci.teams')
