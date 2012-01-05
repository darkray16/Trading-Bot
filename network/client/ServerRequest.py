class ServerRequest(object):
    
    def __init__(self, addr=None, requestBody=None):
        self.addr = addr
        self.requestBody = requestBody
        self.requestLength = 0
        self.username = None
        self.password = None
        self.responseBody = None
        
        if not self.requestBody:
            self.buildBody()
        
    def flush(self):
        self.requestBody = None
        self.requestLength = None
        self.responseBody = None
        
    def execute(self):
        pass
        
    def buildBody(self):
        pass
        
    