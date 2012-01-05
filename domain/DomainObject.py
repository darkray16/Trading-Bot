
class DomainObject(object):
    
    def __init__(self, id=None):
        self.id = id
    
    def get_id(self):
        return self.id
        
    @classmethod
    def get_collection(cls, type):
        return CollectionFactory.getCollection( type )
        
    def collection(self):
        return self.getCollection( type( self ) )
        
    @classmethod
    def get_mapper(cls, adapter, table):
        dsn = ApplicationHelper.getDSN()
        return MapperFactory.get_mapper(adapter, table, dsn)
    
    def get_mapper(self, adapter, table):
        return self.__class__.get_mapper(adapter, table)