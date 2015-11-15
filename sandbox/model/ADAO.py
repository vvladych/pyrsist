from sandbox.model.DAO import DAO, DAOList, consistcheck
from sandbox.helpers.db_connection import dbcursor_wrapper

import psycopg2
import uuid

class ADAO(DAO):    

    @staticmethod
    def fabric_method(row=None):
        adao=ADAO()
        adao.uuid=row.uuid
        adao.a=row.a
        return adao

    data_fields=["uuid","a"]
    entity="ADAO"
    
    def save(self):
        sql_save="""INSERT INTO adao (uuid,a) VALUES( %s, %s);"""
        data=(self.uuid, self.a,)        
        with dbcursor_wrapper(sql_save, data) as cursor:
            pass
        
   