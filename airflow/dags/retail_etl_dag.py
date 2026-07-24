import sys

sys.path.append("/opt/project")


from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime

from src.pipeline import run_pipeline


default_args = {
    "owner": "retail_analytics",
    "start_date": datetime(2026, 7, 24)
}


with DAG(
    dag_id="smart_retail_etl_pipeline",
    default_args=default_args,
    schedule="@daily",
    catchup=False
) as dag:


    run_etl = PythonOperator(
        task_id="execute_retail_etl",
        python_callable=run_pipeline
    )


    run_etl