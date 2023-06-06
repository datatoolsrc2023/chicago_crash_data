#!/usr/bin/python3
from task_utils import helpers


def main():

    sql = helpers.get_sql_from_file('postgresql/vehicles.sql')

    try:
        with helpers.db_cnx() as cnx, cnx.cursor() as c:
            print('attempting to create vehicles table...')
            c.execute(sql)
    except Exception as e:
        raise Exception('unable to create vehicles table') from e
    else:  # no exception
        print('successfully created vehicles table')
    finally:
        cnx.close()


if __name__ == '__main__':
    main()
