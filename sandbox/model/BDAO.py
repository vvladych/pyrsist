from sandbox.model.DAO import DAO, DAOList, consistcheck
from sandbox.helpers.db_connection import dbcursor_wrapper

import psycopg2
import uuid

class BDAO(DAO):

    data_fields=["uuid","b"]
    entity="BDAO"
