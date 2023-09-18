FROM python:3.9.5-slim-buster
RUN apt-get update \
    && apt-get -y install libpq-dev gcc vim poppler-utils

# set work directory
WORKDIR /usr/src/app

COPY ./requirements.txt /code/requirements.txt
RUN pip install -U pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

