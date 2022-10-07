import pandas as pd
import sqlalchemy

# Connect to the database using the connection URI
connection_uri = "postgresql://[user[:password]@][host][:port][/database]"
db_engine = sqlalchemy.create_engine(connection_uri)

# Query using pandas
# Documentation https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html
query = "SELECT * FROM public.football_league"
# Can be used as query or table name
table_name = "football_league"
soccer_df = pd.pandas.read_sql(table_name,
                               db_engine,
                               index_col=None,
                               coerce_float=True,
                               params=None,
                               parse_dates=None,
                               columns=["team_name"],
                               chunksize=None)

print(soccer_df.head(5))

#  Result
#        team_name
# 0       LIVERPOOL
# 1         CHELSEA
# 2  MANCHESTERCITY
# 3         ARSENAL
# 4       LIVERPOOL