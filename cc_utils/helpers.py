from . import db_config, paths
import psycopg2
from psycopg2.extras import DictCursor


def db_cnx(host=db_config.host,
           user=db_config.user,
           password=db_config.password,
           dbname=db_config.database,
           cursor_factory=DictCursor,
           **kwargs):
    return psycopg2.connect(user=user, host=host, password=password,
                            dbname=dbname, cursor_factory=cursor_factory,
                            **kwargs)


def get_sql_from_file(filename):
    # TODO handle comments
    filename = paths.sql / filename
    sql_str = ''

    with open(filename) as f:
        sql = f.read()

    statements = [s.strip().replace('\n', ' ') for s in sql.split(';')]
    sql_str = ';'.join(statements)

    return sql_str
