import uuid

class DAO(object):
    
    def __init__(self, sql_dict):
        self.__uuid=uuid.uuid4()
        self.__sql_dict=sql_dict
        
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
        
    def load(self):
        pass
        
    def save(self):
        pass
        
    def set_object_data(self):
        raise NotImplementedError("set_object_data still not implemented!")
        
    def delete(self):
        pass
        

class DAOList(set):

    def __init__(self, sql_dict, DAO):
        super(DAOList, self).__init__()
        self.__sql_dict=sql_dict
        self.__dao_type=DAO.__class__

    def add(self, DAO):
        if not isinstance(DAO, self.__dao_type):
            raise NotImplementedError("cannot add, type doesn't match %s %s" % (self.__dao_type, DAO.__class__))
        super(DAOList, self).add(DAO)

    def load_all(self, limit=None, orderby=None):
        pass
