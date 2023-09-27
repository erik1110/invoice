import asyncio
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from etl.invoice import InvoiceETL

args = {
    'owner': 'MyInvoice',
}

with DAG(
        dag_id='invoice_auto_carrier',
        default_args=args,
        schedule_interval='10 * * * *',
        start_date=datetime(2023, 8, 1, 0, 0, 0) - timedelta(days=1),
        end_date=datetime(2023, 12, 31, 0, 0, 0) - timedelta(days=1),
        tags=['Invoice'],
        max_active_runs=1,
        concurrency=1,
        catchup=False
) as dag:

    def get_carrier_invoices_header():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(InvoiceETL.get_carrier_invoices_header())
        loop.close()

    def get_carrier_invoices_detail():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(InvoiceETL.get_carrier_invoices_detail())
        loop.close()

    get_carrier_invoices_header = PythonOperator(
            task_id='get_carrier_invoices_header',
            python_callable=get_carrier_invoices_header,
    )

    get_carrier_invoices_detail = PythonOperator(
            task_id='get_carrier_invoices_detail',
            python_callable=get_carrier_invoices_detail,
    )

    get_carrier_invoices_header >> get_carrier_invoices_detail
