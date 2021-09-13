import requests
import pandas as pd
import sqlalchemy

"""
API ENDPOINT DESCRIPTIONS
https://medium.com/@frenzelts/fantasy-premier-league-api-endpoints-a-detailed-guide-acbd5598eb19

SQL

CREATE TABLE "kaido.kariste".fantasy_premierleague
(
    id        integer,
    surname   varchar,
    firstname varchar,
    gametime  timestamp WITH TIME ZONE,
    form      numeric,
    bps       integer,
    price     integer,
    inserted_dtime timestamptz default now()
);


SELECT id, surname, firstname, form, round(avg(bps), 1) AS average_bps,
       price / 10::numeric AS price,
       round(form/(price / 10::numeric),2) as f_to_p
FROM (
         SELECT row_number() OVER (PARTITION BY id ORDER BY gametime DESC) AS rank, *
         FROM "kaido.kariste".fantasy_premierleague) raw
WHERE raw.rank <= 3
GROUP BY id, surname, firstname, form, price
ORDER BY avg(bps) DESC, form DESC;
"""

fantasy_results = []

def pg_connect():
    """
    Connects to Postgres database. Returns connection handler.
    connection_uri = "postgresql://<username>:<PASS>@<HOST>:5432/<DB>"
    """
    connection_uri = ""
    return sqlalchemy.create_engine(connection_uri)

def df_fantasy(engine):
    r = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    bs = r.json()
    players = bs['elements']
    for p in players:
        stats = "https://fantasy.premierleague.com/api/element-summary/{}/".format(p['id'])
        r = requests.get(stats)
        json_response = r.json()
        #gameweek history where is stat for every gameweek
        gwh = json_response['history']
        for bps in gwh:
            lst_values = [p['id'],p['second_name'],p['first_name'], bps['kickoff_time'], p['form'], bps['bps'],p['now_cost']]
            fantasy_results.append(lst_values)
            #print(lst_values)
    # Create the pandas DataFrame
    df = pd.DataFrame(fantasy_results, columns = ['id', 'surname','firstname','gametime','form','bps','price'])
    print(df)
    cur = engine.connect().execution_options(autocommit=True)
    cur.execute("""TRUNCATE TABLE "kaido.kariste".fantasy_premierleague""")

    df.to_sql(name="fantasy_premierleague", con=engine, schema='kaido.kariste', if_exists='append', index=False, chunksize=10000)

if __name__ == '__main__':
    pgdb = pg_connect()
    df_fantasy(pgdb)