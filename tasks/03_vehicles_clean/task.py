#!/usr/bin/python3
from task_utils import helpers


def main():
    sql = helpers.get_sql_from_file('postgresql/clean_vehicles_raw.sql')

    try:
        with helpers.db_cnx() as cnx, cnx.cursor() as c:
            print('attempting to clean vehicles_raw data '
                  'and insert into vehicles table...')
            c.execute(sql)
    except Exception as e:
        raise Exception('unable to insert into vehicles table') from e
    else:  # no exception
        print('successfully inserted into vehicles table')
    finally:
        cnx.close()


if __name__ == '__main__':
    main()
