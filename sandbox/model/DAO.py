import uuid
import psycopg2.extras
from sandbox.helpers.db_connection import get_db_connection

class DAO(object):
    
    entity=None
    @staticmethod
    def fabric_method(row=None):
        print("unimplemented")
    
    data_fields=["uuid"]
    
    def __init__(self):
        self.__uuid=uuid.uuid4()
        #self.data_fields=["uuid"]
        self.sql_dict={}
        for p in self.data_fields:
            setattr(self, p, None)

        
    def __str__(self):
        return "%s" % self.__dict__
    
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
        


def typecheck(func):
    def func_wrapper(*args,**kwargs):
        if not isinstance(args[1], args[0].dao_class):
            raise BaseException("cannot add, type doesn't match %s %s" % (args[0], args[0].dao_class.__name__))
        return func(*args)
    return func_wrapper
    
def consistcheck(s=None):
    def wrap(f):
        def func_wrapper(*args):            
            if not hasattr(args[0].dao,"entity") or args[0].dao.entity==None:
                raise NotImplementedError("entity for dao %s is None" % args[0].dao_class)
            if not s in args[0].sql_dict or args[0].sql_dict[s]==None:
                raise NotImplementedError("%s in sql_dict not available" % s)
            return f(*args)
        return func_wrapper
    return wrap
    
def dbcursor(s=None):
    def wrap(f):
        def func_wrapper(*args):            
            if not hasattr(args[0].dao,"entity") or args[0].dao.entity==None:
                raise NotImplementedError("entity for dao %s is None" % args[0].dao_class)
            if not s in args[0].sql_dict or args[0].sql_dict[s]==None:
                raise NotImplementedError("%s in sql_dict not available" % s)
            return f(*args)
        return func_wrapper
    return wrap            
    
class DAOList(set):

    __LOAD_LIST_SQL_KEY_NAME="load"
        
    def __init__(self, DAO):
        super(DAOList, self).__init__()
        self.dao=DAO
        self.dao_class=DAO.__class__        
        self.sql_dict={DAOList.__LOAD_LIST_SQL_KEY_NAME:"SELECT %s FROM %s;"}

    @typecheck
    def add(self, DAO):
        super(DAOList, self).add(DAO)
        
    @typecheck
    def remove(self, DAO):
        super(DAOList, self).remove(DAO)
                

    @consistcheck("load")
    def load(self, limit=None, orderby=None):
        print(self.sql_dict[self.__LOAD_LIST_SQL_KEY_NAME] % (",".join(self.dao.data_fields), self.dao.entity))
        cursor = get_db_connection().cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
        cursor.execute(self.sql_dict[self.__LOAD_LIST_SQL_KEY_NAME] % (",".join(self.dao.data_fields), self.dao.entity))
        rows=cursor.fetchall()
        for row in rows:
            self.add(self.dao_class.fabric_method(row))
        cursor.close()
