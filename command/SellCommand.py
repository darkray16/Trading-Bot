from Command import *
from command_signals import *

class SellCommand(Command):
    """
    This will handle all tasks in a single selling trade session
    from starting the trade, to closing the trade.  Post-trade
    tasks, like changing customer records are NOT included.
    """
    
    def execute(self, registry):
        """
        @session_registry: registry object that contains application-wide
        variables.
        """
        pre_sell_mode.send(self.__class__)
        
        self.complete_sale()