#Normal functions can also be used.
# However, in this case, the self object will not be send when calling them and it will not be accessible.

class MyClass:
    x = 10
    y = 20
    def Test(self,value):
        return ((self.x+self.y)/2 == value)
def MyFunction( v1,v2): #trebuie sa lipseasca "self" de aici
    return str(v1+v2)
m = MyClass()
print (m.Test(15),m.Test(16))
m.Test = MyFunction
print (m.Test(1,2))