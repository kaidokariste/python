import requests

#https://medium.com/@frenzelts/fantasy-premier-league-api-endpoints-a-detailed-guide-acbd5598eb19

r = requests.get("https://statsapi.web.nhl.com/api/v1/standings")
json_response = r.json()