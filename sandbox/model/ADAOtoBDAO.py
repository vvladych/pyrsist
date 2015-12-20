from sandbox.model.DAO import DAO, DAOList, DAOtoDAO, consistcheck
from sandbox.helpers.db_connection import dbcursor_wrapper

import psycopg2
import uuid

class ADAOtoBDAO(DAOtoDAO):

    entity="adao_to_bdao"
    primDAO_PK="adao_uuid"
    secDAO_PK="bdao_uuid"
