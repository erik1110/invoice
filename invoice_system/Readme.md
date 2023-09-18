[![python37](https://img.shields.io/badge/Python-3.9-blue)]()
<div>

  <img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white">
  <img src="https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white">

</div>

# 查詢發票

## Getting Started
```
# Launch the dev mode
docker-compose up -d

# Stop the dev mode
docker-compose down
```

## Airflow (Build the database for the first time)
```
# Enter Postgres
docker exec -it postgres psql -U postgres

# Create Schema
CREATE DATABASE invoice;

# Initial the airflow
sh ./airflow/init_airflow_setup.sh

```