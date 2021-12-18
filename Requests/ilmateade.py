import requests
from bs4 import BeautifulSoup
import dateutil.parser
from datetime import datetime, timedelta
import pytz

utc=pytz.timezone('Europe/Tallinn')

f = open("weatherbenchmark.txt", "r")
weather = dateutil.parser.parse(f.read()) + timedelta(minutes=6)
now = utc.localize(datetime.now())

# If now becomes greater than weather plus time delta, then run query
if weather < now:
    print(weather)
    print(now)
    print(type(now - weather))
    print ("Weather on väiksem kui now")
else:
    pass



