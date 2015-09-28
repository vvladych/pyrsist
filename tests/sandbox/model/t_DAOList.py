import unittest
from sandbox.model.DAO import DAO,DAOList

class t_DAOList(unittest.TestCase):

    def test_add(self):
        a=DAOList()
        self.assertRaises(BaseException, a.add, None)
        b=DAO()
        a.add(b)
        for d in a:
            print(d)
        self.assertEquals(a.size(), 1)
        # DAO already in list
        #self.assertRaises(BaseException, a.add, b)


suite=unittest.TestLoader().loadTestsFromTestCase(t_DAOList)
unittest.TextTestRunner(verbosity=2).run(suite)
