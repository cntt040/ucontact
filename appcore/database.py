from playhouse.postgres_ext import *
from playhouse.migrate import *

from settings import get_config


conn = get_config('connection')
pg_conf = conn.get('postgres')

database = Proxy()

db_conn = PostgresqlExtDatabase(pg_conf['name'], host=pg_conf['host'], user=pg_conf['username'],
                                password=pg_conf['password'], port=pg_conf['port'], register_hstore=False)

migrator = PostgresqlMigrator(db_conn)

database.initialize(db_conn)


class BaseModel(Model):
    class Meta:
        database = database


