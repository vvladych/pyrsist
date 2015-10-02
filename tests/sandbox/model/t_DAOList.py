import unittest
from sandbox.model.DAO import DAO,DAOList

class t_DAOList(unittest.TestCase):

    def test_add(self):
        l = DAOList(DAO(None))
        a=DAO(None)
        b=DAO(None)
        l.add(a)
        m = DAOList(DAO(None))
        m.add(b)
        self.assertTrue(len(l^l)==0)
        self.assertTrue(len(l^m)>0)
        
    def test_add_none(self):
        l = DAOList(DAO(None))
        self.assertRaises(BaseException, l.add, None)


suite=unittest.TestLoader().loadTestsFromTestCase(t_DAOList)
unittest.TextTestRunner(verbosity=2).run(suite)
