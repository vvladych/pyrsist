from sandbox.model.DAO import DAO, DAOList
from sandbox.model.ADAO import ADAO
import os
import logging
from sandbox.helpers.config_helper import discover_config, read_config
from sandbox.helpers.CONST import CONST
from sandbox.helpers import config
from sandbox.helpers.db_connection import get_db_connection, get_uuid_from_database


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
    a.load()
    adao_list=DAOList(a)
    adao_list.add(a)
    try:
        adao_list.add(d)
    except BaseException as exc:
        print(exc)
    dl.add(a)
    adao_list.load()
    for a in adao_list:
        print("DAS IST A, sicher!!!: %s" % a)
    print("uuid: %s" % get_uuid_from_database())
    try:
        a1=ADAO()
        a1.a="test"
        print("vor dem save")
        a1.save()
        print("saved")
    except BaseException as ex:
        print(ex)
    a2=ADAO("41cc8197-9643-4a0f-8b9d-0881356411ff")
    print(a2)