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


def snowflake_read(df, tablename, engine):
    # https://docs.snowflake.com/en/user-guide/sqlalchemy.html#using-the-snowflake-sqlalchemy-toolkit-with-the-python-connector
    con = engine.connect()
    print(df)
    read_string = "select count(1) FROM {} where id = {};".format(tablename, df.loc[0]['id'])
    print("[INFO] snowflake read: " + read_string)
    results = con.execute(read_string).fetchone()
    if results[0] == 0:
        try:
            df.to_sql(tablename, con=engine, index=False, if_exists='append')
        finally:
            con.close()
            engine.dispose()
    else:
        print('[INFO] snowflake read: Row with id {} already exists, skipping insert ..'.format(results[0]))
        con.close()
        engine.dispose()


def snowflake_insert(df, tablename, engine):
    # https://docs.snowflake.com/en/user-guide/sqlalchemy.html#using-the-snowflake-sqlalchemy-toolkit-with-the-python-connector
    con = engine.connect()
    print(df)
    try:
        df.to_sql(tablename, con=engine, index=False, if_exists='append')
    finally:
        con.close()
        engine.dispose()


def snowflake_update(df, tablename, engine):
    # https://docs.snowflake.com/en/user-guide/sqlalchemy.html#using-the-snowflake-sqlalchemy-toolkit-with-the-python-connector
    con = engine.connect()
    print(df)
    print(df.loc[0]['id'])
    delete_string = "DELETE FROM {} where id = {}".format(tablename, df.loc[0]['id'])
    print(delete_string)
    try:
        con.execute(delete_string)
        df.to_sql(tablename, con=engine, index=False, if_exists='append')
    finally:
        con.close()
        engine.dispose()


def kafka_consumer(topic):
    engine = sqlalchemy.create_engine(URL(
        account='cloudaddress.gcp',
        user='username',
        password='pass',
        database='poc',
        schema='uci',
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
        payload_op = message.value['payload']['op']
        print("Message payload: {}".format(payload_op))
        columns = message.value['payload']['after']
        print(columns)
        df = pd.json_normalize(columns)
        if payload_op == 'c':
            snowflake_insert(df, 'teams', engine)
        elif payload_op == 'u':
            snowflake_update(df, 'teams', engine)
        elif payload_op == 'r':
            snowflake_read(df, 'teams', engine)
        else:
            print("Operation {} not defined".format(payload_op))


if __name__ == '__main__':
    read_config()
    # print(g_workdir)
    print(config)
    kafka_consumer('cyclo.uci.teams')
