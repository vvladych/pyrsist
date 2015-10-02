from model.DAO import DAO, DAOList
from model.ADAO import ADAO, ADAOList
import os
import logging
from helpers.config_helper import discover_config, read_config
from helpers.CONST import CONST

if __name__=="__main__":
    logging.basicConfig(filename=CONST.LOGGER_FILE_NAME, level=logging.DEBUG)
    config = read_config(__file__)
    logging.warn(config.getint('S','a'))
    d=DAO(None)
    dl=DAOList(DAO(None))
    dl.add(d)
    try:
        dl.add(None)
    except BaseException as exc:
        print(exc)
    dl.add(d)
    a=ADAO()
    adao_list=ADAOList()
    adao_list.add(a)
    try:
        adao_list.add(d)
    except BaseException as exc:
        print(exc)
    dl.add(a)
    adao_list.load_all()