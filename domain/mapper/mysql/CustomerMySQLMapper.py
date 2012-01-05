
class CustomerMySQLMapper(MySQLMapper):
	
    def getCollection(self, raw):
        return CustomerCollection(raw, self)
        
    def doCreate(self, data):
        obj = Customer(data["id"], data["name"])
        obj.set_credits(data["credits"])
        obj.set_transactions(data["transactions"])
        obj.set_comments(data["comments"])
        return obj
