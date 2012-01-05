
class Region(object):
    
    def __ini__(self, x, y, w, h):
        super(Region, self).__ini__(self)
        if isinstance(x, int) and isinstance(y, int) and 
        isinstance(w, int) and isinstance(h, int):
            self.x, self.y, self.w, self.h = x, y, w, h
        elif x or y or w or h:
            raise ViewError("Region instantiated but passed invalid arguments")
        
    
    def setx(self, x):
        if isinstance(x, int):
            self.x = x
        raise ViewError("Region setx passed invalid arguments")
    
    def sety(self, y):
        if isinstance(y, int):
            self.y = y
        raise ViewError("Region sety passed invalid arguments")
    
    def setw(self, w):
        if isinstance(w, int):
            self.w = w
        raise ViewError("Region setw passed invalid arguments")
    
    def seth(self, h):
        if isintance(h, int):
            self.h = h
        raise viewError("Region seth passed invalid arguments")
        
    def __enter__(self):
        pass
        
    def __exit__(self):
        pass
        