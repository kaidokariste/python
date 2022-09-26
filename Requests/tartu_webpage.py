import requests
from bs4 import BeautifulSoup
import dateutil.parser
from dateutil.tz import gettz


def get_tartu_articles():
    tartu_benchmark = 'Thu, 22 Sep 2022 07:48:00 +0000'
    dates = []
    fleep_message = ''
    currentbenchmark = ''
    # List of excluded topics
    aripaev_benchmark = dateutil.parser.parse(tartu_benchmark)
    r = requests.get("https://tartu.ee/et/rss")
    soup = BeautifulSoup(r.content, features='lxml-xml')
    articles = soup.findAll('item')

    for a in articles:
        pubDate = a.find('pubDate').text.strip()
        isodate = dateutil.parser.parse(pubDate)
        # Konverdime UTC aja Tallinna aega
        isodate_tallinn = isodate.astimezone(gettz("Europe/Tallinn"))
        #category = a.find('category').text.strip()
        # Get only news where date is newer than current saved benchmark and category is not excluded
        if aripaev_benchmark < isodate:
            title = a.find('title').text.strip()
            description = a.find('description').text.strip()
            description = description.replace('<span class="field field--name-uid field--type-entity-reference field--label-hidden"><span>','').replace('</span></span>','')
            link = a.find('link').text.strip()
            #Preparing fleep message
            fleep_message = fleep_message + '*{}<<{}>>*\n`{} | Tartu uudised | Tartu`\n{}\n\n'.format(link,title,isodate_tallinn.strftime("%H:%M %d.%m.%Y"),description)
            #Forward to fleep sending task
            # ti.xcom_push(key='latest_news', value=fleep_message)
            print(fleep_message)
            dates.append(isodate)
    try:
        currentbenchmark = max(dates)
    except ValueError:
        pass

    tartu_benchmark = currentbenchmark.strftime("%Y-%m-%d %H:%M:%S%z")
    print(tartu_benchmark)

if __name__ == '__main__':
    get_tartu_articles()