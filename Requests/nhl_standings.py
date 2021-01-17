import requests


def nhl_anaheim_ducks_report(r):
    teams = json_response['records'][2]['teamRecords']

    for team in teams:
        if team['team']['name'] == 'Anaheim Ducks':
            # print(team)
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
    requests.post("<fleep_hook>",
    json={"message": message, "user": "NHL"})


if __name__ == "__main__":
    r = requests.get("https://statsapi.web.nhl.com/api/v1/standings")
    json_response = r.json()
    nhloverview = nhl_anaheim_ducks_report(json_response)
    post_fleep(nhloverview)
