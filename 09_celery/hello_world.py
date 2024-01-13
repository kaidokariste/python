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
        'args': (17, 18)
    }
}

@app.task
def add_numbers(a, b):
    z = a + b
    print("Summa on: " + str(z))
    return z



