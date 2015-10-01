from model.DAO import DAO, DAOList
import os
import logging
from helpers.config_helper import discover_config, read_config
from helpers.CONST import CONST

if __name__=="__main__":
    logging.basicConfig(filename=CONST.LOGGER_FILE_NAME, level=logging.DEBUG)
    config = read_config(__file__)
    logging.warn(config.getint('S','a'))
    d=DAO(None)
    dl=DAOList(None,DAO(None))
    dl.add(d)
    try:
        dl.add(None)
    except BaseException as exc:
        print(exc)
    dl.add(d)