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

### Installation
1. Clone this repo.
1. Create a Python virtual environment and install requirements:
```
$ cd chicago_traffic_crashes
$ python -m venv venv
$ source venv/bin/activate
$ python -m pip install -r requirements.txt
```
1. Rename `orchestration/.env-example` to `.env` and update values.
1. Rename `dbt_models/profiles-example.yml` to `profiles.yml` and update values.

### Running the code

To run the code manually:
`$ cd chicago_traffic_crashes/orchestration`
`$ python3 main.py`

This will immediately kick off a run of the full pipeline:
1. Fetch crashes, people, and vehicles CSVs from the Chicago Open Data Portal website
1. Load the data from the CSVs into local `[resource]_raw` PostgreSQL tables.
1. Run dbt models to transform raw data and load into `[resource]_stg` tables.
1. Run dbt models to create analytics views using `[resource]_stg` tables.

To run the pipeline on a schedule, run the Prefect server with `prefect server`. The default schedule is once a day at midnight central time, but can be adjusted in `deployment.py`.
