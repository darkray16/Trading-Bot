import os, sys

sys.path.append(os.path.abspath("adapters/"))

def get_cv_adapter(self, adapter):
	"""
    will return an adapter class which will
    contain all view commands mapped to computer
    vision library specified
    """
    adapters = {
        "sikuli": Sikuli,
        "opencv": OpenCV
    }
    from adapters[adapter] import *
    
    return adapter[adapter]()