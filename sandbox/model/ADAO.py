from sandbox.model.DAO import DAO
from sandbox.model.DAOtoDAO import DAOtoDAOList
from sandbox.model.ADAOtoBDAO import ADAOtoBDAO


class ADAO(DAO):

    data_fields = ["uuid", "a"]
    entity = "ADAO"
    join_objects = {"ADAOtoBDAO": ADAOtoBDAO}

    def __init__(self, uuid=None):
        super(ADAO, self).__init__(uuid)

    def addBDAO(self, bdao):
        """

        :type bdao: object of type BDAO
        """
        self.ADAOtoBDAO.add(ADAOtoBDAO(self.uuid, bdao.uuid))
        #self.join_objects_list["ADAOtoBDAO"].add(ADAOtoBDAO(self.uuid, bdao.uuid))
