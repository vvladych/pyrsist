from model.DAO import DAO, DAOList

class ADAO(DAO):

    def __init__(self):
        super(ADAO, self).__init__(self)
        
class ADAOList(DAOList):

    def __init__(self):
        super(ADAOList, self).__init__(self, ADAO())