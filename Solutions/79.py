class digit(object):
    def __init__(self,name,order):
        self.name = name
        self.order = order
    def __lt__(self,other):
        if self.order < other.order:
            return True
        return False

        
