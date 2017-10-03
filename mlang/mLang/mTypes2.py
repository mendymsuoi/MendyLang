class Dictionary:
    def __init__(self,  keysAndValues):
        self.keys=[]
        self.values=[]
        if len(keysAndValues)%2!=0:
            for i in range(len(keysAndValues)):
                if i%2==0:
                    self.keys.append(keysAndValues[i])
                self.values.append(keysAndValues[i])
        else:
            special=keysAndValues[len(keysAndValues)-1]
            keysAndValues.remove(special)
            for i in range(len(keysAndValues)):
                if i%2==0:
                    self.keys.append(keysAndValues[i])
                self.values.append(keysAndValues[i])
            self.keys.append(special)
            self.values.append(None)
    def Add(self, key, value):
        if key not in self.keys:
            self.keys.append(key) 
            self.values.append(value)
    Reset=__init__
        
d=Dictionary([1, 2, 3, 4, 5, 5])
Reset(d, 1, 2, 3, 4)
print(Dictionary([1, 2, 3, 4, 5, 5]).Reset(1, 2, 3, 4).keys)
# def sum(*args):
#     result=0
#     for argument in args:
#         result = result + 1
#     return result