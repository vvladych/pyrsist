import uuid

class DAO(object):

    __uuid=None
    __entity=None
    __data_dict=None
    __sql_dict=None
    
    
    def __init__(self):
        self.__uuid=uuid.uuid4()
        print(self.__uuid)
        if self.__data_dict!=None:
            self.__dict__[property]=None

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

    def set(self,property,value):
        print("hier mit property %s value %s" % (property,value))
        if property=="__uuid" or property=="_DAO__uuid":
            self.__dict__["__uuid"]=value
            return
        if self.__data_dict is None:
            raise BaseException("data dictionary __data_dict still unimplemented, cannot set")
        if not property in self.__data_dict:
            raise BaseException("cannot set property %s because not in __data_dict" % (property))
        self.__dict__[property]=value
        
    def __setattr__(self,attrname,attrvalue):
        self.set(attrname,attrvalue)

    def __getattr__(self, attrname):
        return self.get(attrname)
        
    def get(self,property):
        print("gette prop: %s" % property)
        if property=="__uuid" or property=="_DAO__uuid":
            return self.uuid()
        if self.__data_dict is None:
            raise BaseException("data dictionary __data_dict still unimplemented, cannot get")
        if not property in self.__data_dict:
            raise BaseException("cannot get property %s because it's not in __data_dict" % property)
        return self.property
        
    def uuid(self):
        return self.__uuid


class DAOList(object):
    __dao_class=DAO().__class__
    __dao_list=[]

    def __init__(self):
        pass
    
    def __eq__(self, other, verbose=False):
        for dao in self.__dao_list:
            if not other.contains(dao):
                if verbose:
                    logger.warn("dao %s exists in self but not in other" % dao)
                return False
        for dao in self.other.__dao_list:
            if not self.contains(dao):
                if verbose:
                    logger.warn("dao %s exists in other but not in self" % dao)
                return False
                
    def __ne__(self,other):
        return not self==other

    def contains(self, DAO):
        if DAO is None:
            raise BaseException("cannot add null object to the daolist")
        if DAO.__class__!=__dao_class:
            raise BaseException("DAO class not match")
        return DAO in self.__dao_list


    def add(self, DAO):
        if DAO is None:
            raise BaseException("cannot add null object to the daolist")
        if DAO in self.__dao_list:
            raise BaseException("already contains DAO %s" % DAO)
        self.__dao_list.append(DAO)

    def size(self):
        return __dao_list.length