from sandbox.model.DAO import DAO
from sandbox.model.DAOtoDAO import DAOtoDAOList
from sandbox.model.ADAOtoBDAO import ADAOtoBDAO


class ADAO(DAO):

    data_fields=["uuid","a"]
    entity="ADAO"
    join_objects_list = dict(ADAOtoBDAO=DAOtoDAOList(ADAOtoBDAO))
        
    def addBDAO(self,BDAO):
        self.join_objects_list["ADAOtoBDAO"].add(ADAOtoBDAO(self.uuid,BDAO.uuid))
