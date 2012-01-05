from Command import *

class LoginCommand(Command):
    """
    Will handle operations for logging into the client software
    """
    
    def execute(self, application_registry):
        """
        @application_registry: registry object that contains application-wide
        variables.
        
        Will handle the task of logging in.  Delegates actual
        interface handling to view.
        """
        
        for value in application_registry.auth_info:
            if not value:
                self.error_msg.add("Missing info: " + str(value))
                
        if self.error_msg:
            raise ErrorHandler('\n'.join(error_msg))
        else:
            login_obj = LoginView()
            
            if login_obj.login():
                login_status = True
            else:
                login_status = False
                
            return login_status