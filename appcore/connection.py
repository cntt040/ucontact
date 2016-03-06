from settings import get_config
import pycouchdb

conn = get_config('connection')
cdb_conf = conn.get('couchdb')

cdb_server = pycouchdb.Server('http://%s:%s/' % (cdb_conf['host'], cdb_conf['port']))

acc_couchdb = cdb_server.database(cdb_conf['database'])

