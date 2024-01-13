import redis

url_connection = redis.from_url("redis://default:*****@redis-16247.c304.europe-west1-2.gce.cloud.redislabs.com:16247")
url_connection.ping()

#url_connection.set('foo', 'bar')
# True

#print(url_connection.get('_kombu.binding.celery'))
# b'bar'
print(url_connection.keys())