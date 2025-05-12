from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

default_args = {"start_date": datetime(year=2023, month=1, day=1),
                "catchup": False}

with DAG(
    dag_id="train_sentiment_model",
    default_args=default_args,
    description="Train sentiment model and log with MLflow",
    tags=["ml", "sentiment"],
) as dag:

    run_training = BashOperator(
        task_id="run_training",
        bash_command="papermill train_models.ipynb output.ipynb"
    )

    run_training
