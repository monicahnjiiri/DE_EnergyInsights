from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['monicjammie@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='etl_storage_dag',
    default_args=default_args,
    description='ETL DAG with email alert on failure',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['etl', 'storage'],
) as dag:

    run_data_storage = BashOperator(
        task_id='run_data_storage',
        bash_command='python /opt/airflow/scripts/DataStorage.py',
    )

    run_data_storage

