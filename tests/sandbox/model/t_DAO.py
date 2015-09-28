import unittest
from sandbox.model.DAO import DAO, DAOList

class t_DAO(unittest.TestCase):

    def test_init(self):
        a=DAO(None)
        print(a.uuid())
        self.assertFalse(a.uuid()==None)

    def test_equals(self):
        a=DAO(None)
        b=a
        self.assertTrue(a==a)
        self.assertTrue(a==b)
        c=DAO(None)
        self.assertFalse(a==c)
        
    def test_s(self):
        l = DAOList(None, DAO(None))
        a=DAO(None)
        b=DAO(None)
        l.add(a)
        m = DAOList(None, DAO(None))
        m.add(b)
        self.assertTrue(len(l^l)==0)
        self.assertTrue(len(l^m)>0)
        


suite=unittest.TestLoader().loadTestsFromTestCase(t_DAO)
unittest.TextTestRunner(verbosity=2).run(suite)