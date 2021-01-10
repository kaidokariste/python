import sqlalchemy
from airflow import DAG
from airflow.operators import PythonOperator
from datetime import datetime, timedelta

# Define the etl function
def insert_to_db_current_date():
    # Connect to the database using the connection URI
    connection_uri = "postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]"
    db_engine = sqlalchemy.create_engine(connection_uri)

    #Define insert statement
    insert_statement = "INSERT INTO dag_insert(kuupaev) values (now())"
    db_engine.execute(insert_statement)

def etl():
    insert_to_db_current_date()

# Following are defaults which can be overridden later on
default_args = {
    'owner': 'kaidokariste',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 10),
    'email': ['kaido@mail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Define the DAG so it runs on a daily basis, after every 5 minutes
dag = DAG(dag_id="home_pc_insert",
          default_args=default_args,
          schedule_interval="*/5 * * * *")

# Make sure `etl()` is called in the operator. Pass the correct kwargs.
task_recommendations = PythonOperator(
    task_id="test_insert_task",
    python_callable=etl,
    dag=dag
    #op_kwargs={"db_engines": db_engines},
)



