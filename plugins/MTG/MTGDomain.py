import DomainObject, Inventory, Customer, Transaction

class InventoryMTGDomain(Inventory.Inventory):
    def set_premium(self, premium):
        """
        premium
            a boolean that represents whether the
            product is a foil, true, or non-foil, false
        """
        self.premium = premium
    def get_premium(self):
        return self.premium
        
        
class CustomerMTGDomain(Customer.Customer):
    pass
    
class TransactionMTGDomain(Transaction.Transaction):
    pass
