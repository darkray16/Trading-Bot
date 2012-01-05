import sys, os, copy
sys.path.append(os.path.abspath("model"))
sys.path.append(os.path.abspath("model/pricelist"))
sys.path.append(os.path.abspath("event"))
from Signal import *
import InventoryAdapter

class CardInventoryModel(object):
    #DAL layer for pricelist for buying and selling single cards
    def __init__(self, dbtype):
        self.inventory_adapter = InventoryAdapter.InventoryAdapter(adapter=dbtype)
        self.inventory = self.inventory_adapter.read_inventory(product="cards")
        
    #set prices is to be done in gui bot settings prior to transaction
    def set_buy_price(self, name, price):
        self.inventory[name]["buy"] = price
    def set_sell_price(self, name, price):
        self.inventiry[name]["sell"] = price
    
    def get_buy_price(self, name):
        return self.inventory[name]["buy"]
    def get_sell_price(self, name):
        return self.inventory[name]["sell"]
    
    def get_stock(self, cardname):
        if len(signals.card_get_stock.receivers) > 0:
            return signals.card_get_stock.send(sender=self.__class__, args=cardname)
        else:
            signals.pre_card_get_stock.send(sender=self.__class__, args=cardname)
            return self.inventory[cardname]["stock"]
        
    def update_stock(self, card):
        if len(signals.card_update_stock.receivers) > 0:
            signals.card_update_stock.send(sender=self.__class__, args=card)
        else:
            signals.pre_card_update_stock.send(sender=self.__class__, args=card)
            self.inventory_adapter.set_stock(product=card)
            self.inventory = self.inventory_adapter.read_inventory_from_db(product="packs")
            signals.post_card_update_stock.send(sender=self.__Class_, args=card)
    
    def get_max_stock(self, cardname):
        return self.inventory[cardname]["max"]
    
    def get_min_stock(self, cardname):
        return self.inventory[cardname]["min"]
    
    def get_card_name_list(self):
        return [cardname for cardname in self.inventory.keys()]
        
    def generate_inventory_file_info(self):
        if len(signals.card_generate_inventory_file_info.receivers) > 0:
            return signals.card_generate_inventory_file_info.send(sender=self.__class__)
        else:
            signals.pre_card_generate_inventory_file_info.send(sender=self.__class__)
            inventory_info = {}
            for productname, productinfo in self.inventory.items():
                inventory_info[productname] = {"max": productinfo["max"], "min": productinfo["min"], "stock": productinfo["stock"], "set": productinfo["set"], "foil": productinfo["foil"]}
            signals.post_card_generate_inventory_file_info.send(sender=self.__class__)
            return inventory_info