from sandbox.model.DAO import DAO
from sandbox.model.DAOtoDAO import DAOtoDAOList
from sandbox.helpers.db_connection import dbcursor_wrapper
from sandbox.model.ADAOtoBDAO import ADAOtoBDAO

import psycopg2
import uuid

class ADAO(DAO):

    data_fields=["uuid","a"]
    entity="ADAO"
    join_objects_list={"ADAOtoBDAO":DAOtoDAOList(ADAOtoBDAO)}
        
    def addBDAO(self,BDAO):
        self.join_objects_list["ADAOtoBDAO"].add(ADAOtoBDAO(self.uuid,BDAO.uuid))
