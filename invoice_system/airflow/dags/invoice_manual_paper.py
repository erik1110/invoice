import asyncio
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from etl.invoice import InvoiceETL

args = {
    'owner': 'MyInvoice',
}

with DAG(
        dag_id='invoice_manual_paper',
        default_args=args,
        schedule_interval='10 * * * *',
        start_date=datetime(2023, 8, 1, 0, 0, 0) - timedelta(days=1),
        end_date=datetime(2023, 9, 30, 0, 0, 0) - timedelta(days=1),
        tags=['Invoice'],
        max_active_runs=1,
        concurrency=1,
        catchup=False
) as dag:
    def invoice_manual_paper():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(InvoiceETL.get_invoice_detail())
        loop.close()

    invoice_manual_paper = PythonOperator(
            task_id='invoice_manual_paper',
            python_callable=invoice_manual_paper,
    )

    invoice_manual_paper
