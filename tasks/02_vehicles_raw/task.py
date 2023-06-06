#!/usr/bin/python3
from task_utils import helpers, paths


def main():

    csv_file = paths.import_files / 'Traffic_Crashes_-_Vehicles.csv'
    # TODO use psycopg2 SQL identifiers
    copy_sql = "COPY vehicles_raw FROM STDIN DELIMITER ',' CSV HEADER"

    try:
        with helpers.db_cnx() as cnx, cnx.cursor() as c, open(csv_file) as f:
            print('attempting to import data into vehicles_raw table')
            c.copy_expert(copy_sql, f)
    except Exception as e:
        raise Exception('could not import data to vehicles_raw table') from e
    else:  # no exception
        print('successfully imported data into vehicles_raw table')
    finally:
        cnx.close()


if __name__ == '__main__':
    main()
