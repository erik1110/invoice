FROM apache/airflow:2.2.4-python3.9

USER root

# Install required packages
RUN apt-get update && \
    apt-get install -y vim && \
    apt-get install -y libpq-dev && \
    apt-get clean

USER airflow

COPY requirements.txt .
# Install additional Python packages
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
