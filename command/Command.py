
class Command(object):
    """
    This is an abstract class.  It is to handle a single task
    requested by the front controller.
    """
    error_messages = []
    
    def execute(self, registry):
        """
        abstract function which should 
        take a Registry object as sole argument.
        Will run command mode with given environment
        variables.
        """
        raise NotImplementedError( "Execute method in " +  type(self).__name__ + " unimplemented")