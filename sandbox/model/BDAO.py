from sandbox.model.DAO import DAO, DAOList, consistcheck
from sandbox.helpers.db_connection import dbcursor_wrapper

import psycopg2
import uuid

class BDAO(DAO):

    data_fields=["uuid","b"]
    entity="BDAO"
    
    def save(self):
        sql_save="""INSERT INTO bdao (uuid,b) VALUES( %s, %s);"""
        data=(self.uuid, self.b,)
        with dbcursor_wrapper(sql_save, data) as cursor:
            pass