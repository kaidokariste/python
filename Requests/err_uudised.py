import requests
from bs4 import BeautifulSoup
import dateutil.parser

dates = []
f = open("newsbenchmark.txt", "r")
currentbenchmark = dateutil.parser.parse(f.read())
print('Failist saadu', currentbenchmark)

r = requests.get("https://www.err.ee/rss")
soup = BeautifulSoup(r.content, features='lxml-xml')
articles = soup.findAll('item')


for a in articles:
    pubDate = a.find('pubDate').text
    isodate = dateutil.parser.parse(pubDate)

    if currentbenchmark < isodate:
        title = a.find('title').text
        description = a.find('description').text
        link = a.find('link').text

        #Preparing fleep message
        message = '*{}<<{}>>*\n`{}`\n{}'.format(link,title,isodate.strftime("%H:%M %d.%m.%Y"),description)
        requests.post("<fleep-web-hook>", json={"message": message, "user": "DWH News Agency"})
        all_news_dates = dates.append(isodate)

try:
    currentbenchmark = max(dates)
except ValueError:
    pass

f = open("newsbenchmark.txt", "w")
f.write(currentbenchmark.strftime("%Y-%m-%d %H:%M:%S%z"))
f.close()