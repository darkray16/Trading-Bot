import os, sys
from registry import *
sys.path.append(os.path.abspath(".."))
sys.path.append(os.path.abspath("registry"))
from ApplicationRegistry import *

class ApplicationHelper(object):
    """
    Does initial setup for application wide variables.
    """ 
    
    @classmethod
    def init(cls):
        """
        Starts all initial work needed when starting App.
        
        Determines the game which decides rest of bot.
        
        Loads ImageHelper which is a mapping class for retrieval
        of images to be used for pattern matching.
        
        Creates Application Registry object which will hold
        all variables that exist until application ends. 
        """
        #do some parsing to figure out what game is being played
        ApplicationRegistry.game = "MTG"
        sys.path.append(os.path.abspath("plugins/" + ApplicationRegistry.game))
        image_helper = __import__("ImageHelper")
        ApplicationRegistry.image_helper = image_helper
        
        #get game specific settings
        sys.path.append(os.path.abspath("plugins/" + ApplicationRegistry.game))
        import settings
        
        #parse the code
        ApplicationRegistry.settings = settings.settings
    
    @classmethod
    def get_setting(cls, key):
        return ApplicationRegisty.key
    
    @classmethod
    def get_gui_lib(cls):
        return "autopy"
        
    @classmethod
    def get_vision_lib(cls):
        return "opencv"
    @classmethod
    def get_inventory_adapter(cls):
        return "txt"