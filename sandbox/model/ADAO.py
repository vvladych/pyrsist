from sandbox.model.DAO import DAO, DAOList

class ADAO(DAO):

    @staticmethod
    def fabric_method(row=None):
        adao=ADAO()
        adao.uuid=row.uuid
        adao.a=row.a
        return adao

    data_fields=["uuid","a"]
        
    def __init__(self):
        super(ADAO, self).__init__()
        self.entity="ADAO"
        
    def __str__(self):
        return "uuid:%s a:%s" % (self.uuid, self.a)
   


        
        
class ADAOList(DAOList):
    
    def __init__(self):
        super(ADAOList, self).__init__(ADAO())