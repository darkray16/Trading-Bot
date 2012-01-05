#handles reading and writing to pricelist files

#MySQL connection settings needed

import sys, os, datetime
sys.path.append(os.path.abspath("model/pricelist"))
sys.path.append(os.path.abspath("model/pricelist/db_adapter"))

import Text

class InventoryAdapter(object):
    def __init__(self, adapter):
        """
        @adapter: string
        sets and initiates functions for adapter
        """
        
        if adapter and isinstance(adapter, str):
            if adapter == "txt":
                self.adapter = Text
            else:
                raise ErrorHandler("No adapter chosen.")
        else:
            raise ErrorHandler("Non-string value passed as adapter to InventoryAdapter.__init__")
    
    def read_inventory(self, product):
        """
        @product: string
        calls the read inventory method for previously specified adapter
        @return: dict
        """
        
        return self.adapter.get_product_info(product)