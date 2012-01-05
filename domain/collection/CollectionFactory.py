import sys, os
sys.path.append(os.path.abspath("../"))
from global_helpers import ApplicationHelper

def get_collection(type):
    game = ApplicationHelper.game
    module = __import__ (game + "Collection")
    
    collection = getattr(module, type + game + "Collection")()
    
    return collection