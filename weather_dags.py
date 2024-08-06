from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

# Importing the task functions
from weather.exctract_air_pollution import main

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'exctract_air_pollution',
    default_args=default_args,
    description='A simple ETL DAG',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
)

# Define the tasks
extract_weather = PythonOperator(
    task_id='extract_pollution',
    python_callable=main,
    dag=dag,
)

# Set the task dependencies
[extract_weather]