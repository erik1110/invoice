#!/bin/sh

# WARNING: Run this script only during initial airflow db setup.

export AIRFLOW_HOME="$(pwd)"
IS_INITDB=True
AIRFLOW_USER=admin
AIRFLOW_PASSWORD=admin
AIRFLOW_USER_EMAIL=test@gmail.com

if [ $IS_INITDB ]; then

  echo "Initializing Airflow DB setup and Admin user setup because value of IS_INITDB is $IS_INITDB"
  echo " Airflow admin username will be $AIRFLOW_USER"

  docker exec -ti airflow_webserver airflow db init && echo "Initialized airflow DB"
  docker exec -ti airflow_webserver airflow users create --role Admin --username $AIRFLOW_USER --password $AIRFLOW_PASSWORD -e $AIRFLOW_USER_EMAIL -f airflow -l airflow && echo "Created airflow Initial admin user with username $AIRFLOW_USER"

else
  echo "Skipping InitDB and InitUser setup because value of IS_INITDB is $IS_INITDB"
fi