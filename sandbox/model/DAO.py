import uuid

class DAO(object):
    
    def __init__(self):
        self.__uuid=uuid.uuid4()
        
    def __str__(self):
        return "%s" % self.__uuid
    
    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other, verbose=False):
        if not other is None and isinstance(other, self.__class__):
            if not verbose or self.__dict__==other.__dict__:
                return self.__dict__==other.__dict__
            else:
                if verbose:
                    msg="%s" % set(self.__dict__)^other.__dict__
                    if logger is not None:
                        logger.warn(msg)
                    else:
                        print(msg)
        return False


    def __ne__(self,other):
        return not self==other
        
    def uuid(self):
        return self.__uuid


