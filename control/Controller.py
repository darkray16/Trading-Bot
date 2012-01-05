import os, sys
sys.path.append(os.path.abspath(".."))
sys.path.append(os.path.abspath("../registry/"))
sys.path.append(os.path.abspath("../command/"))

from global_helpers import ApplicationHelper
from command import CommandResolve
from controller_signals import *
from registry import *

class Controller(object):
	
    def __init__(self):
        ApplicationHelper.init()
    
    def login(self):
        """
        Login to client program, modifies registry
        to reflect post login status
        """
        login_command = CommandFactory.get_command(pre_login.send(sender=self.__class__))
        if not login_command:
            login_command = CommandFactory.get_command("Login")
        
        login_status = login_command.execute(self.application_registry["auth_info"])
        if login_status:
            return
        else:
            raise CommandError("Login failed")
        
    def main(self):
        """
        runs main loop that will handle trading and trading
        related functions of the bot.
        """
        
        """
        pre_main_loop signal should supply the name of a  command class to use instead of 
        StartTrade if you wish to use custom trade commands.  Then you must create a custom 
        command in place of StartTrade, and set your custom command trade mode to the name of it.
        """
        pluggable_trade_starter = pre_main_loop.send(sender=self.__class__)
        
        if pluggable_trade_starter:
            trade_starter = CommandResolve.get_command(pluggable_trade_starter)
        else:
            trade_starter = CommandResolve.get_command(request="StartTrade")
        while True:
            #this signal 
            signal_response = pre_main.send(sender=self.__class__)
            self.session_registry = TradeSessionRegistry()
            #wait for trade then accept
            trade_starter.execute(self.session_registry)
            session_command = CommandResolve.get_command(self.session_registry.get("trade_mode"))
            
            if not session_command:
                raise ControlError("SessionCommand was not be created")
            
            session_command.execute(self.session_registry)
            
            cleanup_command = main_session_cleanup.send(sender=self.__class__)
            if cleanup_command is not None:
                CommandResolve.get_command(cleanup_command)
            if not cleanup_command:
                cleanup_command = CommandResolve.get_command("TradeCleanup")
            
            cleanup_command.execute(self.session_registry)
            del(self.session_registry)
            post_main.send(sender=self.__class__)
        
        post_main_loop.send(sender=self.__class__)
    
    def run(self, login=None):
        """
        Main controller that will contain application-wide logic.
        
        login
            set to true if you wish the bot to login
        """
        if login:
            self.login()
        self.main()