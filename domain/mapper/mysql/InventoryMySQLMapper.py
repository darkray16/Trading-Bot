
class InventoryMySQLMapper(MySQLMapper):

    def getCollection(self, raw):
        return InventoryCollection(raw, self)
        
    def doCreate(self, data):
        obj = Inventory(data["id"])
        obj.set_name(data["premium"])
        obj.set_set(data["premium"])
        obj.set_premium(data["premium"])
        obj.set_buy_price(data["buy_price"])
        obj.set_sell_price(data["sell_price"])
        obj.set_current_stock(data["current_stock"])
        obj.set_max_stock(data["max_stock"])
        obj.set_min_stock(data["min_stock"])
        return obj