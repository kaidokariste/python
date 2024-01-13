import logging
import random

from celery import Celery
from celery.schedules import crontab

app = Celery('matemaatika',
             broker='redis://default:***@redis-16247.c304.europe-west1-2.gce.cloud.redislabs.com:16247')

# add "add_numbers" task to the beat schedule
# Task is in form <module_name>.<task_function>
app.conf.beat_schedule = {
    "liitmine": {
        "task": "hello_world.add_numbers",
        "schedule": crontab(),
        'args': (random.randint(0, 20), 1)
    },
    "korrutamine": {
        "task": "hello_world.multiply",
        "schedule": crontab()
    }
}


@app.task
def add_numbers(a, b):
    z = a + b
    logging.info(f'Juhuslik liidetav {a} , summa {z}')
# When no return, the log will say
# Task hello_world.add_numbers[8e042b82-bb86-4e04-abda-61303bbead1c] succeeded in 0.015000000013969839s: None


@app.task
def multiply():
    a = random.randint(1, 9)
    b = random.randint(1, 15)
    z = a * b
    logging.info(f'a = {a}, b = {b}, Korrutis:  {z}')
    return z

#The log
# [2024-01-13 20:52:00,116: INFO/MainProcess] Task hello_world.multiply[522ba790-cc53-4765-9e92-afa74c5b934b] received
# [2024-01-13 20:52:00,118: INFO/MainProcess] a = 8, b = 5, Korrutis:  40
# [2024-01-13 20:52:00,135: INFO/MainProcess] Task hello_world.multiply[522ba790-cc53-4765-9e92-afa74c5b934b] succeeded in 0.01600000000325963s: 40
