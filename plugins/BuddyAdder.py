from sikuli.Sikuli import *
path_to_bot = getBundlePath().rsplit("\\", 1)[0] + "\\"

exec(open(path_to_bot + "ini.py", "rb").read())

sys.path.append(path_to_bot + "model")
sys.path.append(path_to_bot + "view")
sys.path.append(path_to_bot + "plugins")

import BuddyRequester

class BuddyAdder(object):
    """
    Class will call buddy requester to get a list of all
    buddies to add.  Buddies will be filtered then added to 
    MTGO buddy list
    """
     
    def __init__(self, requester):
        self.requester = requester
    
    def request_buddies(self):
        self.self.requester.request_buddy()
        
    def accept_buddy(self, buddy_name):
        #filter buddies...
        pass
        
    def add_buddy_to_list(self, buddy_name):
        buddies = self.request_buddies
        self.buddies = self.accept_buddies(buddies)
        
        #add buddies...