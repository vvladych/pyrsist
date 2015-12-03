from sandbox.model.DAO import DAO, DAOList
from sandbox.model.ADAO import ADAO
from sandbox.model.BDAO import BDAO
import os
import logging
from sandbox.helpers.config_helper import discover_config, read_config
from sandbox.helpers.CONST import CONST
from sandbox.helpers import config
from sandbox.helpers.db_connection import get_db_connection, get_uuid_from_database


def test_db_conn():
    conn=get_db_connection()
    

def testSuite1():
    d=DAO()
    dl=DAOList(DAO)
    dl.add(d)
    try:
        dl.add(None)
    except BaseException as exc:
        print(exc)
    dl.add(d)
    a=ADAO()
    adao_list=DAOList(ADAO)
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
    uuid_to_load=None
    try:
        a1=ADAO()
        a1.a="test"
        print("vor dem save")
        a1.save()
        uuid_to_load=a1.uuid()
        print("saved")
    except BaseException as ex:
        print(ex)
    a2=ADAO(uuid_to_load)
    print(a2)
    for dao in adao_list:
        print("delete first adao record from the list: %s" % dao.uuid)
        dao.delete()
        print("done!")
        break    
    
if __name__=="__main__":
    logging.basicConfig(filename=CONST.LOGGER_FILE_NAME, level=logging.DEBUG)
    logging.warn(config.getint('S','a'))
    print(config.getint('S','a'))
    testSuite1()
    
    adao_list=DAOList(ADAO)
    adao_list.load()
    adao=None

    for a in adao_list:
        adao=a
        adao.load()
        break
    
    print(adao)
    adao=ADAO()
    adao.a="trululu"
    print(adao)
    adao.save()
    adao.a="bababa"
    adao.update()
    b=BDAO()
    b.b="hier ist b!"
    adao.addBDAO(b)
    print(adao)