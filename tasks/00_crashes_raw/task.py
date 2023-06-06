#!/usr/bin/python3
from task_utils import helpers, paths


def main():

    # sql = helpers.get_sql_from_file('postgresql/import_crashes_raw.sql')
    csv_file = paths.import_files / 'Traffic_Crashes_-_Crashes.csv'
    # table = "crashes_raw"
    # TODO use psycopg2 SQL identifiers
    copy_sql = "COPY crashes_raw FROM STDIN DELIMITER ',' CSV HEADER"

    try:
        with helpers.db_cnx() as cnx, cnx.cursor() as c, open(csv_file) as f:
            print('attempting to import data into crashes_raw table')
            c.copy_expert(copy_sql, f)
    except Exception as e:
        raise Exception('could not import data to crashes_raw table') from e
    else:  # no exception
        print('successfully imported data into crashes_raw table')
    finally:
        cnx.close()


if __name__ == '__main__':
    main()
