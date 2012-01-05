from DomainObject import *

class Inventory(DomainObject):
	
    def __init__(self, id):
        super(self.__class__, self).__init__(id)
        
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
        
    def set_set(self, set):
        self.set = set
    def get_set(self):
        return self.set
        
        
    def set_buy_price(self, price):
        self.buy_price = price
    def get_buy_price(self):
        return self.buy_price
    
    def set_sell_price(self, price):
        self.sell_price = price
    def get_sell_price(self):
        return self.sell_price
        
    def set_current_stock(self, stock):
        self.current_stock = stock
    def get_current_stock(self):
        return self.current_stock
    
    def set_max_stock(self, stock):
        self.max_stock = stock
    def get_max_stock(self, stock):
        return self.max_stock
    
    def set_min_stock(self, stock):
        self.min_stock = stock
    def get_min_stock(self):
        return self.min_stock