import os
from prefect import get_run_logger
import psycopg2
from psycopg2 import sql
import requests


def import_csv(resource, csv_url):
    '''
    Delete existing CSV from /tmp, then
    fetch CSV from Chicago Open Data Portal
    and load to /tmp.
    '''

    # TODO in production, load to S3 or GCS bucket)
    # TODO have a separate function/Op to clear /tmp
    # before any CSV imports run

    csv_file = f'tmp/{resource}.csv'
    if os.path.exists(csv_file):
        os.remove(csv_file)

    with open(csv_file, 'wb') as f, requests.get(csv_url, stream=True) as r:
        for line in r.iter_lines():
            f.write(line + '\n'.encode())

    return csv_file


def db_cnx(host=os.getenv("TC_PG_HOST"),
           dbname=os.getenv("TC_PG_DB_NAME"),
           user=os.getenv("TC_PG_USERNAME"),
           password=os.getenv("TC_PG_PASSWORD"),
           return_str=False):
    '''
    Create and return Postgres database connection.
    TODO get port from environment variables
    '''
    conn_string = f'postgresql://{user}:{password}@{host}:5432/{dbname}'
    if return_str:
        return conn_string
    else:
        return psycopg2.connect(conn_string)


def get_sql_from_filename(filename):
    '''
    Return SQL as string from SQL file.
    '''

    # TODO handle comments
    full_filename = f'sql/{filename}.sql'
    sql_str = ''

    with open(full_filename) as f:
        sql = f.read()

    statements = [s.strip().replace('\n', ' ') for s in sql.split(';')]
    sql_str = ';'.join(statements)

    return sql_str


def load_csv_to_db(sql_file, csv_file, tablename):
    '''
    Create table if not exists, truncate table,
    then load data from CSV file to table.
    '''

    logger = get_run_logger()

    create_query = get_sql_from_filename(sql_file)
    truncate_query = 'TRUNCATE TABLE {}'
    copy_query = "COPY {} FROM STDIN DELIMITER ',' CSV HEADER"

    try:
        with db_cnx() as cnx, cnx.cursor() as c, open(csv_file) as f:
            c.execute(create_query)
            # use SQL identifiers to safely construct these queries
            c.execute(sql.SQL(truncate_query).
                      format(sql.Identifier(tablename)))
            c.copy_expert(sql.SQL(copy_query).
                          format(sql.Identifier(tablename)),
                          f)
    except Exception as e:
        raise e
    else:
        logger.info(f'{tablename} table created and loaded with data')
    finally:
        cnx.close()
