from Command import *
from command_signals import *

class BuyCommand(Command):
    """
    This will handle all tasks in a single buying trade session
    from starting the trade, to closing the trade.  Post-trade
    tasks, like changing customer records are NOT included.
    """
    
    def execute(self, registry):
        """
        @session_registry: registry object that contains application-wide
        variables.
        """
        pre_buy_mode.send(self.__class__)
        self.complete_purchase(registry)