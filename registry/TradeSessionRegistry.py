from Registry import *

class TradeSessionRegistry(dict):
    
    def get(self, key):
        return self[key]
        
    def set(self, key, value):
        self[key] = value