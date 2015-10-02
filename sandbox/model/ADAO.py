from model.DAO import DAO, DAOList

class ADAO(DAO):

    data_dict=("common_name")
    entity="ADAO"

    def __init__(self):
        super(ADAO, self).__init__(self)
        
        
class ADAOList(DAOList):
    
    sql_dict={"load_all":"SELECT %s FROM %s"}

    def __init__(self):
        super(ADAOList, self).__init__(ADAO())