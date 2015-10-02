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
        
class t_ConcreteDAO(unittest.TestCase):

    class ConcreteDAO(DAO):
        def __init__(self):
            super(t_ConcreteDAO.ConcreteDAO, self).__init__(self)            
        
    def test_concrete_dao(self):
        a=t_ConcreteDAO.ConcreteDAO()
        b=DAO(None)
        self.assertFalse(a==b)

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(t_DAO))
suite.addTest(unittest.makeSuite(t_ConcreteDAO))
unittest.TextTestRunner(verbosity=2).run(suite)