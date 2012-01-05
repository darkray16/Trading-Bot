
class TransactionMySQLMapper(MySQLMapper):
	
    
    def getCollection(self, raw):
        return TransactionCollection(raw, self)
    
    def doCreate(self, data):
        obj = Transaction(data["id"])
        obj.setTime(data["time"])
        obj.set_customer_name(data["name"])
        obj.set_products(data["products"])
        return obj