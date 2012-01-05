from Command import *

class TradeCleanupCommand(Command):
    
    def execute(self, session_registry):
        
        self.cleanup(session_registry)
        return
        
