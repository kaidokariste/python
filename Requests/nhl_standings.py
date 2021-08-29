import requests

def nhl_anaheim_ducks_report(r):
    teams_records = json_response['records']
    for tr in teams_records:
        if tr['division']['id'] == 27:
            teams = tr['teamRecords']
            #print(teams)
            for team in teams:
                if team['team']['name'] == 'Anaheim Ducks':
                    teamname = team['team']['name']
                    wins = team['leagueRecord']['wins']
                    losses = team['leagueRecord']['losses']
                    ot = team['leagueRecord']['ot']
                    points = team['points']
                    leaguerank = team['leagueRank']
                    streak = team['streak']['streakCode']
    ducksReport = ("::: \n %s record (%i-%i-%i) %i pts, current streak %s and is ranked %sth in NHL " % (
                 teamname, wins, losses, ot, points, streak, leaguerank))

    return ducksReport


def post_fleep(message):
    requests.post("<fleep-conversation-hook>",
                  json={"message": message, "user": "NHL"})


if __name__ == "__main__":
    r = requests.get("https://statsapi.web.nhl.com/api/v1/standings")
    json_response = r.json()
    nhloverview = nhl_anaheim_ducks_report(json_response)
    print(nhloverview)
    post_fleep(nhloverview)
