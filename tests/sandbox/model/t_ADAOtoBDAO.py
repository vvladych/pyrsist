import unittest
from sandbox.helpers.transaction_broker import transactional
from sandbox.model.ADAO import ADAO
from sandbox.model.BDAO import BDAO
from sandbox.model.ADAOtoBDAO import ADAOtoBDAO

class t_ADAOtoBDAO(unittest.TestCase):


    @transactional
    def test_read_write_adaotobdao(self):
        adao=ADAO()
        adao.save()
        bdao=BDAO()
        bdao.save()
        adao.addBDAO(bdao)
        adao.save
        #adao.delete()
        #bdao.delete()

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(t_ADAOtoBDAO))
unittest.TextTestRunner(verbosity=2).run(suite)