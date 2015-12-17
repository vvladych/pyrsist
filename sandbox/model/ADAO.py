from sandbox.model.DAO import DAO, DAOList, DAOtoDAO, consistcheck
from sandbox.helpers.db_connection import dbcursor_wrapper
from sandbox.model.ADAOtoBDAO import ADAOtoBDAO

import psycopg2
import uuid

class ADAO(DAO):

    data_fields=["uuid","a"]
    entity="ADAO"
    join_objects_list={"ADAOtoBDAO":DAOList(ADAOtoBDAO)}
    adao_to_bdao_list=DAOList(ADAOtoBDAO)
    
    def __str__(self):
        retA=" ".join(list(map(lambda x:"%s:%s" % (x,getattr(self,x)), self.data_fields)))        
        retL=" ".join(list(map(lambda x:"%s:%s" % ("adao_to_bdao",x.secDAO.uuid), self.adao_to_bdao_list)))        
        return "{ %s %s }" % (retA, retL)
        
    def addBDAO(self,BDAO):
        self.join_objects_list["ADAOtoBDAO"].add(ADAOtoBDAO(self,BDAO))
