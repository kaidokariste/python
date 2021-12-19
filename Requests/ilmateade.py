import requests
from bs4 import BeautifulSoup
import dateutil.parser
from datetime import datetime, timedelta
import pytz


def weather_forecast():
    fleep_message = ''
    utc = pytz.timezone('Europe/Tallinn')

    f = open("weatherbenchmark.txt", "r")
    weather = dateutil.parser.parse(f.read()) + timedelta(minutes=1)
    now = utc.localize(datetime.now())

    vaatlusandmed = requests.get('https://www.ilmateenistus.ee/ilma_andmed/xml/observations.php')
    tartu_emhi = 'https://www.ilmateenistus.ee/asukoha-prognoos/?coordinates=58.3800520744161;26.7221159100379'
    soup = BeautifulSoup(vaatlusandmed.content, features='lxml-xml')
    stations = soup.findAll('station')


    for st in stations:
        stationCode = st.find('wmocode').text
        if stationCode == '26242':
            temp = st.find('airtemperature').text
            windspeed = st.find('windspeed').text
            relativehumidity = st.find('relativehumidity').text
            phenomenon = st.find('phenomenon').text

    fleep_message = '*{}<<Tartu>>*\n`{} | emhi ilm`\n Temperatuur: {}\n Tuulekiirus: {} m/s\n Õhuniiskus: {}%,\n Olu: {}'.format(
        tartu_emhi, now.strftime("%H:%M %d.%m.%Y"), temp, windspeed, relativehumidity, phenomenon)

    # If now becomes greater than weather plus time delta, then run query
    if weather < now:
        print(fleep_message)
        requests.post("<fleep-web-hook>", json={"message": fleep_message, "user": "DWH News Agency"})
        f = open("weatherbenchmark.txt", "w")
        f.write(now.strftime("%Y-%m-%d %H:%M:%S%z"))
        f.close()
    else:
        pass

if __name__ == '__main__':
    weather_forecast()
