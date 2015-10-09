
import psycopg2

__all__ = ['get_db_connection']

dbInstance=None

def get_db_connection():
    global dbInstance    
    if dbInstance is None:
        dbInstance=psycopg2.connect("dbname=daotest user=vvladych password=vvladych")
    return dbInstance

