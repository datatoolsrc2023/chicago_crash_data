import asyncio
import common
import os
from prefect import flow, task
from prefect_dbt.cli.commands import DbtCoreOperation


# Global settings
csv_urls = {
    'crashes': 'https://data.cityofchicago.org/api/views/85ca-t3if/rows.csv?accessType=DOWNLOAD&api_foundry=true',
    'people': 'https://data.cityofchicago.org/api/views/u6pd-qa9d/rows.csv?accessType=DOWNLOAD&api_foundry=true',
    'vehicles': 'https://data.cityofchicago.org/api/views/68nd-jvt3/rows.csv?accessType=DOWNLOAD&api_foundry=true'
}


"""
Crashes tasks
"""


@task
def get_crashes_csv(resource, csv_url):
    # Delete existing crashes CSV from /tmp
    # Fetch crashes CSV from Chicago Open Data Portal and load to /tmp
    # TODO in production, load to S3 or GCS bucket
    csv_file = common.import_csv(resource, csv_url)
    return csv_file


@task
def load_crashes_raw(sql_filename, csv_file, tablename):
    # Load raw crashes data to crashes_raw table
    common.load_csv_to_db(sql_filename, csv_file, tablename)


"""
People tasks
"""


@task
def get_people_csv(resource, csv_url):
    # Delete existing people CSV from /tmp
    # Fetch people CSV from Chicago Open Data Portal and load to /tmp
    # TODO in production, load to S3 or GCS bucket
    csv_file = common.import_csv(resource, csv_url)
    return csv_file


@task
def load_people_raw(sql_filename, csv_file, tablename):
    # Load raw people data to people_raw table
    common.load_csv_to_db(sql_filename, csv_file, tablename)


"""
Vehicle tasks
"""


@task
def get_vehicles_csv(resource, csv_url):
    # Delete existing vehicles CSV from /tmp
    # Fetch vehicles CSV from Chicago Open Data Portal and load to /tmp
    # TODO in production, load to S3 or GCS bucket
    csv_file = common.import_csv(resource, csv_url)
    return csv_file


@task
def load_vehicles_raw(sql_filename, csv_file, tablename):
    # Load raw vehicles data to vehicles_raw table
    common.load_csv_to_db(sql_filename, csv_file, tablename)


"""
All flows
"""


@flow
async def crashes_flow(csv_urls):
    csv_file = get_crashes_csv('crashes',  csv_urls['crashes'])
    load_crashes_raw('crashes_raw', csv_file, 'crashes_raw')


@flow
async def people_flow(csv_urls):
    csv_file = get_people_csv('people',  csv_urls['people'])
    load_crashes_raw('people_raw', csv_file, 'people_raw')


@flow
async def vehicles_flow(csv_urls):
    csv_file = get_vehicles_csv('vehicles',  csv_urls['vehicles'])
    load_vehicles_raw('vehicles_raw', csv_file, 'vehicles_raw')


@flow
def dbt_clean_and_load():
    # dbt models flow
    # these dbt models transform data in the raw tables
    # and insert cleaned data into the resource-named tables
    # (crahes, vehicles, people)
    project_dir = os.getenv("CHICAGO_CRASHES_DBT_PROJECT")
    profiles_dir = os.getenv("CHICAGO_CRASHES_DBT_CONFIG")
    result = DbtCoreOperation(
        commands=["dbt run", "dbt debug"],
        project_dir=project_dir,
        profiles_dir=profiles_dir
    ).run()
    return result


@flow
async def main_flow():
    #parallel_subflows = [crashes_flow(csv_urls), people_flow(csv_urls),
    #                     vehicles_flow(csv_urls)]
    #await asyncio.gather(*parallel_subflows)
    dbt_clean_and_load()


if __name__ == '__main__':
    main_flow_state = asyncio.run(main_flow())
