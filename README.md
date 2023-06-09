# Chicago traffic crashes

Code to clean and perform exploratory data analysis on traffic crash datasets provided by the City of Chicago:
* [Crashes](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if)
* [Vehicles](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Vehicles/68nd-jvt3)
* [People](https://data.cityofchicago.org/Transportation/Traffic-Crashes-People/u6pd-qa9d)

## Tools

* Orchestration and raw data fetching / loading: [Prefect](https://docs.prefect.io/2.10.13/)
* Raw data transformations: [dbt](https://docs.getdbt.com/)
* Database: [PostgreSQL](https://www.postgresql.org/docs/)


## Setup

### Prerequisites
1. Install PostgreSQL
1. Optionally create a dedicated Postgres user and database for this project (I created a db called `traffic_crashes`, then created a user `crash` with a separate password and granted the user on the database and all tables in it.)

### Installation steps
1. Clone this repo.
1. Create a Python virtual environment and install requirements:
```
$ cd chicago_traffic_crashes
$ python -m venv venv
$ python -m pip install -r requirements.txt
```
1. Rename `orchestration/.env-example` to `.env` and update values.
1. Rename `dbt_models/profiles-example.yml` to `profiles.yml` and update values.
