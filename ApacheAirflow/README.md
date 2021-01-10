# Docker
Running container and exposing 5432 (Postgres) for connection  
`docker run -d -p 8080:8080 -p 5432:5432 -v C:\airflow\dags:/usr/local/airflow/dags  puckel/docker-airflow webserver`