
class Collection(object):
	
    def __init__(self, raw, mapper):
        self.pointer = 0
        self.total = 0
        
        if raw and mapper:
            self.raw = raw
            self.total = len(raw)
            
        self.mapper = mapper
        
    def add(self, object):
        if isinstance(object, DomainObject):
            target_class = self.target_class()
            if not isinstance(object, target_class):
                raise CollectionError("Non-" + str(target_class) + " passed to add")
            self.notify_access()
            self.objects[self.total] = object
            self.total += 1
    
    def target_class(self):
        raise NotImplementedError("target_class on object " + self.__name__ + " not implememented")
    
    def get_row(self, num):
        self.notify_access()
        if num >= self.total or num is 0:
            return None
        if self.objects[num]:
            return self.objects[num]
        if self.raw[num]:
            self.objects[num] = self.mapper.createObject(self.raw[num])
            return self.objects[num]
        return None
    
    def rewind(self):
        self.pointer = 0
        
    def current(self):
        return self.get_row(self.pointer)
        
    def pointer(self):
        return self.pointer
        
    def next(self):
        row = self.get_row(self.pointer)
        if row:
            self.pointer += 1
        return row
    
    def valid(self):
        row = self.get_row(self.pointer)
        if row is not None:
            return True
        else:
            return False
