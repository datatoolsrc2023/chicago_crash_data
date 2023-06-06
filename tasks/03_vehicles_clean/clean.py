#!/usr/bin/env python3
from task_utils import helpers


def main():
    '''Drop vehicles table'''

    query = 'drop table if exists vehicles'

    try:
        with helpers.db_cnx() as cnx, cnx.cursor() as c:
            print('attempting to drop vehicles table...')
            c.execute(query)
    except Exception as e:
        raise Exception('unable to drop vehicles table') from e
    else:
        print('successfully dropped vehicles table')
    finally:
        cnx.close()


if __name__ == '__main__':
    main()
