import sys, os
sys.path.append(os.path.abspath("../"))
from ApplicationRegistry import *

def make_command(comm_name):
    """
    searches for a module for the specified game which will contain
    all the necessary commands needed for it.
    """
    sys.path.append(os.path.abspath("../plugins/" + ApplicationRegistry.game))
    m = __import__ (ApplicationRegistry.game + "Commands")
    
    comm = getattr( m, str(comm_name) + ApplicationRegistry.game + "Command" )()
    is_command(comm)
    
    return comm
    
def is_command(kls):
    """
    check to make sure subclass inherits from Command.  Duck typing.
    """
    if kls.execute:
        return
    else:
        CommandError("CommandFactory passed a class which doesn't contain execute() method")
