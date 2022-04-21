import requests
from bs4 import BeautifulSoup
import dateutil.parser
from dateutil.tz import gettz


def aripaev_news():
    dates = []
    # List of excluded topics
    exclude_topics = ['Sisuturundus']

    f = open("aripaevbenchmark.txt", "r")
    currentbenchmark = dateutil.parser.parse(f.read())
    #print('Initial benchmark', currentbenchmark)

    r = requests.get("http://feeds.feedburner.com/aripaev-rss")
    soup = BeautifulSoup(r.content, features='lxml-xml')
    articles = soup.findAll('item')

    for a in articles:
        pubDate = a.find('pubDate').text.strip()
        isodate = dateutil.parser.parse(pubDate)
        # Konverdime UTC aja Tallinna aega
        isodate_tallinn = isodate.astimezone(gettz("Europe/Tallinn"))
        category = a.find('category').text.strip()
        # Get only news where date is newer than current saved benchmark and category is not excluded
        if currentbenchmark < isodate and category not in exclude_topics:
            title = a.find('title').text.strip()
            description = a.find('description').text.strip()
            link = a.find('link').text.strip()
            #Preparing fleep message
            message = '*{}<<{}>>*\n`{} | {} | Äripäev`\n{}'.format(link,title,isodate_tallinn.strftime("%H:%M %d.%m.%Y"),category, description)
            requests.post("<fleep-web-hook>", json={"message": message, "user": "DWH News Agency"})
            dates.append(isodate)
    try:
        currentbenchmark = max(dates)
    except ValueError:
        pass

    f = open("aripaevbenchmark.txt", "w")
    f.write(currentbenchmark.strftime("%Y-%m-%d %H:%M:%S%z"))
    f.close()

if __name__ == '__main__':
    aripaev_news()
