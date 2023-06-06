#!/usr/bin/env python3
from task_utils import helpers


def main():
    '''Drop vehicles_raw table'''

    query = 'drop table if exists vehicles_raw'

    try:
        with helpers.db_cnx() as cnx, cnx.cursor() as c:
            print('attempting to drop vehicles_raw table...')
            c.execute(query)
    except Exception as e:
        raise Exception('unable to drop vehicles_raw table') from e
    else:
        print('successfully dropped vehicles_raw table')
    finally:
        cnx.close()


if __name__ == '__main__':
    main()
