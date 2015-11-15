from sandbox.model.DAO import DAO, DAOList, consistcheck
from sandbox.helpers.db_connection import dbcursor_wrapper

import psycopg2
import uuid

class ADAO(DAO):

    data_fields=["uuid","a"]
    entity="ADAO"
    
    def save(self):
        sql_save="""INSERT INTO adao (uuid,a) VALUES( %s, %s);"""
        data=(self.uuid, self.a,)        
        with dbcursor_wrapper(sql_save, data) as cursor:
            pass
        
   