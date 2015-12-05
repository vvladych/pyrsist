import unittest
from sandbox.helpers.transaction_broker import transactional
from sandbox.model.ADAO import ADAO


class t_ADAO(unittest.TestCase):


    @transactional
    def test_read_write_adao(self):
        adao=ADAO()
        print(adao)
        adao_uuid=adao.uuid
        adao.a="a"
        adao.save()
        print(adao)
        adao_2=ADAO(adao_uuid)
        print(adao_2)
        self.assertTrue(adao_2.a=="a")
        adao_2.a="a2"
        adao_2.update()
        adao_3=ADAO(adao_uuid)
        print(adao_3)
        self.assertTrue(adao_3.a=="a2")
        adao_3.delete()
        self.assertRaises(BaseException, ADAO, adao_uuid)
        

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(t_ADAO))
unittest.TextTestRunner(verbosity=2).run(suite)