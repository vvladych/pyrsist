import unittest
from sandbox.model.DAO import DAO

class t_DAO(unittest.TestCase):

    def test_init(self):
        a=DAO()
        print(a.uuid())
        self.assertFalse(a.uuid()==None)

    def test_equals(self):
        a=DAO()
        b=a
        self.assertTrue(a==a)
        self.assertTrue(a==b)
        c=DAO()
        self.assertFalse(a==c)
        


suite=unittest.TestLoader().loadTestsFromTestCase(t_DAO)
unittest.TextTestRunner(verbosity=2).run(suite)