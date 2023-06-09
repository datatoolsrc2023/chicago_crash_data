# Chicago traffic crashes

Code to clean and perform exploratory data analysis on traffic crash datasets provided by the City of Chicago:
* [Crashes](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if)
* [Vehicles](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Vehicles/68nd-jvt3)
* [People](https://data.cityofchicago.org/Transportation/Traffic-Crashes-People/u6pd-qa9d)

## Tools

* Orchestration and raw data fetching / loading: [Prefect](https://docs.prefect.io/2.10.13/)
* Raw data transformations: [dbt](https://docs.getdbt.com/)
* Database: [PostgreSQL](https://www.postgresql.org/docs/)