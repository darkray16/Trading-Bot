from DomainObject import *

class Transaction(DomainObject):
	
    def __init__(self, id):
        super(self.__class__, self).__init__(id)
        self.take = []
        self.give = []
    
    def set_time(self, time):
        pass
        
    def get_time(self):
        pass
        
    def set_customer_name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise DomainError("non-string passed to set_customer_name")
        
    def get_customer_name(self):
        return self.customer_name

    def add_products(self, product):
        if isinstance(product, Product):
            self.products.add( product )
        else:
            raise DomainError("non-Product passed to add_products")
    
    def add_product(self, product):
        self.products.append(product)
        
    def take_product(self, product):
        if isinstance(product, Product):
            self.take.append(product)
        else:
            raise DomainError("non-Product passed to take_product")
            
    def give_product(self, product):
        if isinstance(product, Product):
            self.give.append(product)
        else:
            raise DomainError("non-Product passed to give_product")
    
    def give_count(self):
        #return number of items giving/giving
        return self.give
        
    def take_count(self):
        #return number of items taking/taken
        return self.take
        
    def cancel(self):
        #clear out all transaction info
        del self.take[:]
        del self.give[:]

class SaleTransaction(Transaction):
    def __init__(self, id): 
        super(self.__class__, self).__init__(id)
        
    
class PurchaseTransaction(Transaction):
    def __init__(self, id): 
        super(self.__class__, self).__init__(id)
    
    