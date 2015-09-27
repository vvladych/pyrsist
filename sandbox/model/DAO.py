import uuid

class DAO(object):

    __uuid=None
    __entity=None
    __sql_dict=None
    
    
    def __init__(self):
        self.__uuid=uuid.uuid4()

    def __eq__(self, other, verbose=False):
        if other is None:
            return False
        if isinstance(other, self.__class__):
            if not verbose or self.__dict__==other.__dict__:
                return self.__dict__==other.__dict__
            else:
                for k in self.__dict__:
                    # TODO: test for existence of k in self/other -> merge lists???
                    if self.k!=other.k:
                        msg="diff: %s in self: %s in other: %s" % (k,self.k,other.k)
                        if logger!=None:
                            logger.warn(msg)
                        else:
                            print(msg)
                return False
        else:
            return False


    def __ne__(self,other):
        return not self==other
        
    def uuid(self):
        return self.__uuid


