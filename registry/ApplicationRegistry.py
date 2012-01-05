from Registry import *
import os, sys

class ApplicationRegistry(Registry):
    settings = {}
    
    @classmethod
    def add_settings(cls, settings):
        cls.settings = settings
    
    @classmethod        
    def __get__(cls, key):
        print str(key)
        return cls.key
        
    @classmethod
    def __set__(cls, key, value):
        try:
            cls.key
        except KeyError:
            cls.key = value
        else:
            raise RegistryError("Attempt to set an existing key.")
        print "key: " + str(key) + " value: " + str(value)
        
    @classmethod
    def update(cls, key, value):
        if cls.settings[key] is None:
            raise RegistryError("Attempt to update a non-existant key.")
        else:
            cls.settings[key] = value
            
    @classmethod
    def get_window_name(cls):
        return "Magic Online"