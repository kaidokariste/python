import requests
from bs4 import BeautifulSoup
import dateutil.parser
import ilmateade as wt

def err_news():
    dates = []
    # List of excluded topics
    exclude_topics = ['Arhitektuur', 'Teater', 'ETV uudised', 'Kunst', 'Raadiouudised', 'Välismaa', 'Inimesed',
                  'ETV spordi lühiuudised','Arvamus']

    f = open("newsbenchmark.txt", "r")
    currentbenchmark = dateutil.parser.parse(f.read())
    # print('Initial benchmark', currentbenchmark)

    r = requests.get("https://www.err.ee/rss")
    soup = BeautifulSoup(r.content, features='lxml-xml')
    articles = soup.findAll('item')


    for a in articles:
        pubDate = a.find('pubDate').text
        isodate = dateutil.parser.parse(pubDate)
        category = a.find('category').text
        # Get only news where date is newer than current saved benchmark and category is not excluded
        if currentbenchmark < isodate and category not in exclude_topics:
            title = a.find('title').text
            description = a.find('description').text
            link = a.find('link').text
            #Preparing fleep message
            message = '*{}<<{}>>*\n`{} | {}`\n{}'.format(link,title,isodate.strftime("%H:%M %d.%m.%Y"),category, description)
            requests.post("<fleep-web-hook>", json={"message": message, "user": "DWH News Agency"})
            dates.append(isodate)

    try:
        currentbenchmark = max(dates)
    except ValueError:
        pass

    f = open("newsbenchmark.txt", "w")
    f.write(currentbenchmark.strftime("%Y-%m-%d %H:%M:%S%z"))
    f.close()

if __name__ == '__main__':
    err_news()
    wt.weather_forecast()