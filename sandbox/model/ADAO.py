from model.DAO import DAO, DAOList

class ADAO(DAO):

    def __init__(self):
        self.data_fields=["uuid", "common_name"]
        self.entity="ADAO"


        
        
class ADAOList(DAOList):
    
    def __init__(self):
        super(ADAOList, self).__init__(ADAO())