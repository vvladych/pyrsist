import uuid
import psycopg2.extras
from sandbox.helpers.db_connection import get_db_connection, dbcursor_wrapper, get_uuid_from_database


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
            # TODO: else: test for entity in db with simple select
            if not s in args[0].sql_dict or args[0].sql_dict[s]==None:
                raise NotImplementedError("%s in sql_dict not available" % s)
            return f(*args)
        return func_wrapper
    return wrap
    

        

class DAO(object):
    
    entity=None
    data_fields=["uuid"]
    
    
    @staticmethod
    def fabric_method(row=None):
        raise NotImplementedError("Not implemented")
    
    def __init__(self):        
        for p in self.data_fields:
            setattr(self, p, None)
        self.uuid=get_uuid_from_database()

        
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
                
    def load(self):
        sql_query_load="""SELECT %s FROM %s WHERE uuid='%s'""" % (",".join(self.__class__.data_fields), self.__class__.entity, self.uuid)
        print(sql_query_load)
        with dbcursor_wrapper(sql_query_load) as cursor:
            row=cursor.fetchone()
            if row!=None:
                print(row)
                for key in row.keys:
                    print(key)
            
        
    def save(self):
        raise NotImplementedError("save still not implemented")
        
    def set_object_data(self):
        raise NotImplementedError("set_object_data still not implemented!")
        
    def delete(self):
        pass
        
    
    
class DAOList(set):

    __LOAD_LIST_SQL_KEY_NAME="load"
        
    sql_dict={__LOAD_LIST_SQL_KEY_NAME:"SELECT %s FROM %s"}    
        
    def __init__(self, DAO):
        super(DAOList, self).__init__()
        self.dao=DAO
        self.dao_class=DAO.__class__        
        

    @typecheck
    def add(self, DAO):
        super(DAOList, self).add(DAO)
        
    @typecheck
    def remove(self, DAO):
        super(DAOList, self).remove(DAO)
                

    @consistcheck("load")
    def load(self):
        query=self.sql_dict[DAOList.__LOAD_LIST_SQL_KEY_NAME] % (",".join(self.dao.data_fields), self.dao.entity)
        with dbcursor_wrapper(query) as cursor:            
            rows=cursor.fetchall()
            for row in rows:
                self.add(self.dao_class.fabric_method(row))
        

class DAOtoDAO(object):

    def __init__(self, primDAO):
        self.primDAO=primDAO
        
    def load(self):
        pass
        
    def setSecDAO(self, secDAO):
        self.secDAO=secDAO
        
    def save(self):
        self.secDAO.save()