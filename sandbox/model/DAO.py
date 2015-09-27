import uuid

class DAO(object):

    __uuid=None
    __entity=None
    __sql_dict=None
    
    
    def __init__(self):
        self.__uuid=uuid.uuid4()

    def __eq__(self, other, verbose=False):
        if not other is None and isinstance(other, self.__class__):
            if not verbose or self.__dict__==other.__dict__:
                return self.__dict__==other.__dict__
            else:
                print("%s" % set(self.__dict__)^other.__dict__)
        return False


    def __ne__(self,other):
        return not self==other
        
    def uuid(self):
        return self.__uuid


