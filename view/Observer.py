import threading

class Observer(threading.Thread):
    def __ini__(self):
        super(Observer, self).__ini__(self)
        self.callables = []
        
    def set_callable(self, callable):
        if hasattr(callable, "__call__"):
            self.callable = callable
        else:
            raise ObserverError("Non-callable passed to add_callable")
            
    def run(self):
        return self.callable()