from sandbox.model.DAOtoDAO import DAOtoDAO


class ADAOtoBDAO(DAOtoDAO):

    entity = "adao_to_bdao"
    primDAO_PK = "adao_uuid"
    secDAO_PK = "bdao_uuid"
