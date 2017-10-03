class Dictionary:
    def __init__(self):
        self.keys=[]
        self.values=[]
        
    def Add(self, *args):
        for arg in args:
            if arg[0] not in self.keys:
                self.keys.append(arg[0])
                self.values.append(arg[1])
            else:
                if input("Key already in dictionary, would you like to overwrite? Y/N").lower.startswith("y"):
                    self.keys.append(arg[0])
                    self.values.append(arg[1])
                else:
                    pass
                
    def Get(self, key):
        atNumber=-1
        for k in range(len(self.keys)):
            if self.keys[k]==key:
                atNumber=k
        return self.values[atNumber]


class String(str):
    def StartsWith(self, list_):
        if type(list_)==List:
            for item in list_.get:
                if self.startswith(item):
                    return item
        elif(type(list_)==String):
            if self.StartsWith(item):
                    return item
        return False
	    
    def Replace(self, old, new,count="all",lr="<"):
        if count=="all":
            return self.replace(old, new)
        if lr==">":
            return (self[::-1].replace(old[::-1], new[::-1], count))[::-1]
        elif lr=="<":
            return self.replace(old, new, count)
	    
	    
class List:
    def __init__(self, typ=None):
        self.get=[]
        self.typ=typ if typ else None
    
        
    def Add(self, whattoadd):
        if self.typ and self.typ!=type(whattoadd):
            raise TypeError("Expected value of type {}, but got {}".format(self.typ, str(type(whattoadd))))
        else:
            self.get.append(whattoadd)
            
    def Concat(self, *args):
        for arg in args:
            if type(arg)==type([]):
                for item in arg:
                    self.get.append(item)
            elif type(arg)==type(List('')):
                for item in arg.get:
                    self.get.append(item)