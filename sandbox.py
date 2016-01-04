from sandbox.model.DAO import DAO, DAOList
from sandbox.model.ADAO import ADAO
from sandbox.model.BDAO import BDAO
from sandbox.model.DAOtoDAO import DAOtoDAOList
from sandbox.model.ADAOtoBDAO import ADAOtoBDAO
import logging
from sandbox.helpers.CONST import CONST
from sandbox.helpers.db_connection import get_db_connection, get_uuid_from_database, dbcursor_wrapper
from sandbox.helpers.transaction_broker import transactional



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

def testsuite2():
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
    adao.save()
    b=BDAO()
    b.b="hier ist b!"
    adao.addBDAO(b)
    print(adao)
    
def testsuite3():
    adao_list = DAOList(ADAO)
    adao_list.load()
    for a in adao_list:
        print(a)
        if a.a == "das ist ein test":
            a.a = "nun 2"
        else:
            a.a = "das ist ein test"
        a.save()
    adao=ADAO()
    adao.a="nun 3"
    adao.save()
    adao.a="und nun 7"
    adao.save()
    adao.delete()
    print(len(adao_list))
    adao=ADAO(adao_list.pop().uuid)
    print(adao)
    print(len(adao_list))
    adao=ADAO()
    bdao=BDAO()
    bdao.save()
    adao.addBDAO(bdao)
    adao.save()
    print(adao)

def testsuite4():
    adao = ADAO()
    adao.a = "a"
    adao.save()
    bdao = BDAO()
    bdao.save()
    adao2 = ADAO()
    adao.addBDAO(bdao)
    adao.save()
    print(adao)
    print(adao2)
    adao_uuid = adao.uuid
    adao3 = ADAO(adao_uuid)
    print(adao3)


@transactional
def tt():
    insert_sql_tmpl = "INSERT INTO %s (%s) VALUES (%s)"
    fieldlist = ["uuid", "text"]
    data = [get_uuid_from_database(), 'Das ist ein Test lalalala']

    insert_sql = insert_sql_tmpl % ("publicationtext", ",".join(fieldlist), ",".join(list(map(lambda x: "%s", data))))

    print(insert_sql)
    with dbcursor_wrapper(insert_sql, data) as cursor:
        pass

if __name__=="__main__":
    logging.basicConfig(filename=CONST.LOGGER_FILE_NAME, level=logging.DEBUG)
    dtd_list1 = DAOtoDAOList(ADAOtoBDAO)
    dtd_list1.load('7f55cf76-e800-4543-a954-c38d5c41dad3')
    dtd_list2 = DAOtoDAOList(ADAOtoBDAO)
    dtd_list2.load('7f55cf76-e800-4543-a954-c38d5c41dad3')
    dtd_diff = dtd_list1 ^ dtd_list2
    testsuite3()