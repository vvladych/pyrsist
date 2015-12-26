import unittest
from sandbox.model.DAO import DAO, DAOList

class t_DAO(unittest.TestCase):

    def test_init(self):
        a = DAO()
        self.assertTrue(a.uuid is not None)

    def test_equals(self):
        a = DAO()
        b = a
        self.assertTrue(a == a)
        self.assertTrue(a == b)
        c = DAO()
        self.assertFalse(a == c)
        
    def test_to_str(self):
        a = DAO()
        self.assertRegex("%s" % a, "uuid:")
        self.assertRegex("%s" % a, "^{.*}$")

class t_ConcreteDAO(unittest.TestCase):

    class ConcreteDAO(DAO):
        def __init__(self):
            super(t_ConcreteDAO.ConcreteDAO, self).__init__()            
        
    def test_concrete_dao(self):
        a = t_ConcreteDAO.ConcreteDAO()
        b = DAO()
        self.assertFalse(a == b)


suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(t_DAO))
suite.addTest(unittest.makeSuite(t_ConcreteDAO))
unittest.TextTestRunner(verbosity=2).run(suite)