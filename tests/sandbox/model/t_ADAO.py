import unittest
from sandbox.helpers.transaction_broker import transactional
from sandbox.model.ADAO import ADAO
from sandbox.helpers.db_connection import get_db_connection


class t_ADAO(unittest.TestCase):

    @transactional
    def test_read_write_adao(self):
        # test insert
        adao = ADAO()
        adao_uuid = adao.uuid
        adao.a = "a"
        adao.save()
        # test load from database
        adao_2 = ADAO(adao_uuid)
        self.assertTrue(adao_2.a == "a")
        adao_2.a = "a2"
        # test update
        adao_2.save()
        self.assertTrue(adao != adao_2)
        adao_3 = ADAO(adao_uuid)
        self.assertTrue(adao_3.a=="a2")
        # test delete
        adao_3.delete()
        # test load
        self.assertRaises(BaseException, ADAO, adao_uuid)
        get_db_connection().rollback()


#suite=unittest.TestSuite()
#suite.addTest(unittest.makeSuite(t_ADAO))
#unittest.TextTestRunner(verbosity=2).run(suite)