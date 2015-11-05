
import psycopg2
from sandbox.helpers import config


__all__ = ['get_db_connection']

dbInstance=None


def get_db_connection():
    global dbInstance
    print("%s" % config.get('dbconnection', 'user'))
    if dbInstance is None:
        dbInstance=psycopg2.connect("""dbname=%s user=%s password=%s""" % (config.get('dbconnection','dbname'), config.get('dbconnection','user'), config.get('dbconnection','password')))
    return dbInstance

    