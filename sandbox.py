from sandbox.model.DAO import DAO, DAOList
from sandbox.model.ADAO import ADAO, ADAOList
import os
import logging
from sandbox.helpers.config_helper import discover_config, read_config
from sandbox.helpers.CONST import CONST
from sandbox.helpers import config
from sandbox.helpers.db_connection import get_db_connection


def test_db_conn():
    conn=get_db_connection()
    

if __name__=="__main__":
    logging.basicConfig(filename=CONST.LOGGER_FILE_NAME, level=logging.DEBUG)
    logging.warn(config.getint('S','a'))
    print(config.getint('S','a'))
    d=DAO()
    dl=DAOList(DAO())
    dl.add(d)
    try:
        dl.add(None)
    except BaseException as exc:
        print(exc)
    dl.add(d)
    a=ADAO()
    adao_list=DAOList(a)
    adao_list.add(a)
    try:
        adao_list.add(d)
    except BaseException as exc:
        print(exc)
    dl.add(a)
    adao_list.load()
    for a in adao_list:
        print(a)