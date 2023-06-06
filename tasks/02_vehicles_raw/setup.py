#!/usr/bin/python3
from task_utils import helpers


def main():
    sql = helpers.get_sql_from_file('postgresql/vehicles_raw.sql')

    try:
        with helpers.db_cnx() as cnx, cnx.cursor() as c:
            print('attempting to create vehicles_raw table...')
            c.execute(sql)
    except Exception as e:
        raise Exception('unable to create vehicles_raw table') from e
    else:  # no exception
        cnx.commit()
        print('successfully created vehicles_raw table')
    finally:
        cnx.close()


if __name__ == '__main__':
    main()
