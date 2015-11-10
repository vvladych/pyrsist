from sandbox.model.DAO import DAO, DAOList

class ADAO(DAO):

    @staticmethod
    def fabric_method(row=None):
        adao=ADAO()
        adao.uuid=row.uuid
        adao.a=row.a
        return adao

    data_fields=["uuid","a"]
    entity="ADAO"
   