# Redis and Celery cron
* Alustame celery installimisega
```python
pip install -U "celery[redis]"
```
* Terminalis 1 Käivitame Celery beatsi (antud juhul pead seda tegam 09_celery kaustas)
  * Sellega paneme sisuliselt crontaby tööle
  * [Celery beats](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html)

```python
celery -A hello_world beat --loglevel=INFO
```

_hello_world_ - fail, kus kogu crontab asub
* Kui beat on käivitunud, on vaja avada järgmine terminal ja käivitada worker.
```python
# Worker for windows, single node
celery -A hello_world worker --pool=solo --loglevel=INFO

# For windows multy node
pip install eventlet
celery -A hello_world worker --pool=eventlet --loglevel=INFO
```
 
    
