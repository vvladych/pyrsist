import uuid
import psycopg2.extras
from sandbox.helpers.db_connection import get_db_connection, dbcursor_wrapper, get_uuid_from_database
from sandbox.helpers.transaction_broker import transactional
from sandbox.helpers.type_guard import typecheck, consistcheck
from sandbox.model.DAOtoDAO import DAOtoDAO


class DAO(object):

    __LOAD_OBJECT_BY_UUID="load"
    __DELETE_OBJECT_BY_UUID="delete"
    __INSERT_OBJECT="insert"
    __UPDATE_OBJECT="update"
        
    sql_dict={__LOAD_OBJECT_BY_UUID:"SELECT %s FROM %s WHERE uuid='%s'",
              __DELETE_OBJECT_BY_UUID:"DELETE FROM %s WHERE uuid='%s'",
              __UPDATE_OBJECT:"UPDATE %s SET %s WHERE uuid='%s'",
              __INSERT_OBJECT:"INSERT INTO %s(%s) VALUES( %%s, %%s );"
              }    
    
    entity=None
    data_fields=["uuid"]
    join_objects_list={}

    def __init__(self, uuid=None):
        self.__is_persisted=False
        for p in self.data_fields:
            setattr(self, p, None)
        if uuid==None:
            self.uuid=get_uuid_from_database()
        else:
            self.uuid=uuid
            self.load()

        
    def __str__(self):
        retA=" ".join(list(map(lambda x:"%s:%s" % (x,getattr(self,x)), self.data_fields)))
        daotodao_list=[]
        for join_object_list in self.join_objects_list.keys():
            list_to_append=self.join_objects_list.get(join_object_list)
            daotodao_list.append("%s: {%s}" % (join_object_list, list_to_append))            
        return "{ %s %s }" % (retA, " ".join(daotodao_list))
    
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
             
    @consistcheck("load")
    def load(self):
        sql_query_load=self.sql_dict[DAO.__LOAD_OBJECT_BY_UUID] % (",".join(self.__class__.data_fields), self.__class__.entity, self.uuid)
        with dbcursor_wrapper(sql_query_load) as cursor:
            row=cursor.fetchone()
            if row!=None:
                for data_field in self.__class__.data_fields:
                    setattr(self, data_field, getattr(row, data_field))
                self.__is_persisted=True
            else:
                raise BaseException("row with uuid %s doesn't exist" % self.uuid)
        # load daotodao objects: not necessary!
        for join_object_list in self.join_objects_list.keys():
            self.join_objects_list[join_object_list].load(self.uuid)

        
    
    @transactional
    def save(self):
        if self.__is_persisted:
            self.__update()
        else:
            self.__insert()

    @consistcheck("insert")
    def __insert(self):
        fieldlist=[]
        data=[]
        for key in self.data_fields:
            fieldlist.append(key)
            data.append(getattr(self,key))
        sql_save=self.sql_dict[DAO.__INSERT_OBJECT] % (self.entity, ",".join(fieldlist))
        with dbcursor_wrapper(sql_save, data) as cursor:
            pass
        self.__is_persisted=True
        for join_object_list in self.join_objects_list.keys():
            for elem in self.join_objects_list.get(join_object_list):
                elem.save()
        

    @consistcheck("update")
    def __update(self):
        psycopg2.extras.register_uuid()
        setstr=",".join(list(map(lambda x:x+"=%("+x+")s", filter(lambda x:x!="uuid", self.data_fields))))
        sql_update=self.sql_dict[DAO.__UPDATE_OBJECT] % (self.entity, setstr, self.uuid)
        h=dict()        
        for f in self.data_fields:
            if f!='uuid':
                h[f]=getattr(self,f)
        with dbcursor_wrapper(sql_update, h) as cursor:
            pass        

    
    @transactional
    @consistcheck("delete")
    def delete(self):
        sql_query=self.sql_dict[DAO.__DELETE_OBJECT_BY_UUID] % (self.__class__.entity, self.uuid)
        with dbcursor_wrapper(sql_query) as cursor:
            pass
            
    


class DAOList(set):

    __LOAD_LIST_SQL_KEY_NAME="load"
        
    sql_dict={__LOAD_LIST_SQL_KEY_NAME:"SELECT %s FROM %s"}   

    def __str__(self):
        elems=[]
        for e in self:
            elems.append("%s" % e)
        return ",".join(elems)
        
    def __init__(self, DAO):
        super(DAOList, self).__init__()
        self.dao=DAO
        self.entity=DAO.entity
        

    @typecheck
    def add(self, DAO):
        super(DAOList, self).add(DAO)
        
    @typecheck
    def remove(self, DAO):
        super(DAOList, self).remove(DAO)

    @consistcheck("load")
    def load(self):
        query=DAOList.sql_dict[DAOList.__LOAD_LIST_SQL_KEY_NAME] % (",".join(self.dao.data_fields), self.entity)
        with dbcursor_wrapper(query) as cursor:
            rows=cursor.fetchall()
            for row in rows:
                self.add(self.dao(getattr(row,'uuid')))
        

