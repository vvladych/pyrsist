from sandbox.model.DAO import DAO, DAOList, DAOtoDAO, consistcheck
from sandbox.helpers.db_connection import dbcursor_wrapper
from sandbox.model.ADAOtoBDAO import ADAOtoBDAO

import psycopg2
import uuid

class ADAO(DAO):

    data_fields=["uuid","a"]
    entity="ADAO"
    adao_to_bdao_list=DAOList(ADAOtoBDAO)
    
    def __str__(self):
        ret="{"
        for attr in self.data_fields:
            ret="""%s %s:%s; """ % (ret, attr, getattr(self, attr))
        for a in self.adao_to_bdao_list:
            ret="""%s; {%s:%s} """ % (ret, "adao_to_bdao", a.secDAO.uuid)
        ret="""%s }""" % ret
        return ret
    
    def save(self):
        sql_save="""INSERT INTO adao (uuid,a) VALUES( %s, %s);"""
        data=(self.uuid, self.a,)        
        with dbcursor_wrapper(sql_save, data) as cursor:
            pass
        
    def addBDAO(self,BDAO):
        adao_to_bdao=ADAOtoBDAO(self)
        adao_to_bdao.setBDAO(BDAO)
        self.adao_to_bdao_list.add(adao_to_bdao)