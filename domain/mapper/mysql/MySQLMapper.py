

class MySQLMapper(object):
	
	def __init__(self, mysql_connect):
		"""
        mysql_connect
            the connection class that will take the queries
            and return results
        """
        self.connection = mysql_connection
    
    def find(self, id):
        results = self.doFind(id)
        if not results or not isinstance(results, list):
            return None
        object = self.createObject(results)
    
    def createObject(self, data):
        obj = self.doCreateObject(data)
        return obj
        
    def insert(self, obj):
        self.doInsert(obj)
    
    def doInsert(self, obj):
        self.db_adapter.insert(obj)
    
    def update(self, obj):
        self.db_adapter.update(obj)
        
    def doFind(self, id):
        return self.db_adapter.find(id)
        
    def doCreate(self, data):
        raise NotImplementedError("doCreate not implemented")