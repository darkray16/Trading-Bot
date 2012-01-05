from Command import *

class StartTradeCommand(Command):
    """
    Waits for a trade request, then handles task of
    accepting the request and determining any variables from request.
    If you wish to use custom trade commands, then you must run custom
    command instead of this command to create and use them.
    """
    
    def execute(self, session_registry):
        """
        this will loop until a trade is requested, then get info
        like customer name, credits, etc.
        @registry: SessionRegistry object that will hold all information
            for this trade session.
        """
        
        self.trade_start(session_registry)
        
        return session_registry