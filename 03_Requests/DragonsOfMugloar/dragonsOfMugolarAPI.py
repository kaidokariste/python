import json
import xml.etree.ElementTree
import requests

# Defineerime mitu korda soovime skripti jooksutada
for x in range(1, 101):

    # Esimese päringuga saame mängu ID ja muutujad, mida võitluses kasutada
    response = requests.get('http://www.dragonsofmugloar.com/api/game')
    data = json.loads(response.text)

    # vastuseks saadud JSON-ist vajalike väärtuse hankimine
    gameId = data['gameId']
    armor = data['knight']['armor']
    attack = data['knight']['attack']
    agility = data['knight']['agility']
    endurance = data['knight']['endurance']

    knight_tuples = [
        ('armor', armor),
        ('attack', attack),
        ('agility', agility),
        ('endurance', endurance)
    ]

    knight_strength = (sorted(knight_tuples, key=lambda knight: knight[1], reverse=True))

    scaleThickness = 0
    wingStrength = 0
    clawSharpness = 0
    fireBreath = 0

    if knight_strength[0][0] == 'attack':
        scaleThickness = knight_strength[0][1]+2
    elif knight_strength[0][0] == 'agility':
        wingStrength = knight_strength[0][1]+2
    elif knight_strength[0][0] == 'armor':
        clawSharpness = knight_strength[0][1]+2
    else:
        fireBreath = knight_strength[0][1]+2

    if knight_strength[1][0] == 'attack':
        scaleThickness = knight_strength[1][1]-1
    elif knight_strength[1][0] == 'agility':
        wingStrength = knight_strength[1][1]-1
    elif knight_strength[1][0] == 'armor':
        clawSharpness = knight_strength[1][1]-1
    else:
        fireBreath = knight_strength[1][1]-1

    if knight_strength[2][0] == 'attack':
        scaleThickness = knight_strength[2][1]-1
    elif knight_strength[2][0] == 'agility':
        wingStrength = knight_strength[2][1]-1
    elif knight_strength[2][0] == 'armor':
        clawSharpness = knight_strength[2][1]-1
    else:
        fireBreath = knight_strength[2][1]-1

    if knight_strength[3][0] == 'attack':
        scaleThickness = knight_strength[3][1]
    elif knight_strength[3][0] == 'agility':
        wingStrength = knight_strength[3][1]
    elif knight_strength[3][0] == 'armor':
        clawSharpness = knight_strength[3][1]
    else:
        fireBreath = knight_strength[3][1]

    # Ilmaennustuse saamine
    weather = 'http://www.dragonsofmugloar.com/weather/api/report/' + str(gameId)

    response_weather = requests.get(weather)

    root = xml.etree.ElementTree.fromstring(response_weather.text)

    # Korjame ilmaennustuse XML-st välja aja ja teate
    time = root[0].text
    code = root[2].text
    message = root[3].text

    # Insert put request
    if code == 'FUNDEFINEDG':  # Fog
        solution = {"dragon": {
            "scaleThickness": 10,
            "clawSharpness": 6,
            "wingStrength": 3,
            "fireBreath": 1}}
    elif code == 'HVA':  # Heavy rain with floods
        solution = {"dragon": {
            "scaleThickness": 5,
            "clawSharpness": 10,
            "wingStrength": 5,
            "fireBreath": 0}}
    elif code == 'T E':  # The long dry
        solution = {"dragon": {
            "scaleThickness": 5,
            "clawSharpness": 5,
            "wingStrength": 5,
            "fireBreath": 5}}
    elif code == 'SRO':  # Storm
        solution = {}
    else:  # Normal weather
        solution = {"dragon": {
            "scaleThickness":  scaleThickness,
            "clawSharpness":  clawSharpness,
            "wingStrength":  wingStrength,
            "fireBreath": fireBreath}}

    web_solution = 'http://www.dragonsofmugloar.com/api/game/' + str(gameId) + '/solution'

    put_solution = requests.put(web_solution, json=solution)

    # Let see how the fight went
    battle = put_solution.content

    # text_file = open("C:/Users/Kaido/Documents/GitProjects/Sandbox/PY/DragonsOfMugloar/Results/Output.txt", "a")
    # Alternatiiv
    text_file = open("C:/Users/kaido.kariste/Documents/Python/PY/DragonsOfMugloar/Results/Output.txt", "a")

    text_file.write("Game#: %s\n" % x)
    text_file.write("GameId: %s\n" % gameId)
    text_file.write("Time %s\n" % time)
    text_file.write("Weather %s\n" % message)
    text_file.write("Weather code %s\n" % code)
    text_file.write("Knight %s\n" % str([armor, attack, agility, endurance]))
    text_file.write("Dragon %s\n" % str(solution))
    text_file.write("Battle %s\n" % battle)
    text_file.write("\n")

    text_file.close()
