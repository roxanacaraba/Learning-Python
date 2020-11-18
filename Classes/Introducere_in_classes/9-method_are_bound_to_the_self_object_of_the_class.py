#Methods are bound to the self object of the class they were initialized in.
# Even if you associate a method from a different class to a new method, the self will belong to the original class.

class MyClass:
    x = 10
    def Test(self,value):
        return ((self.x+self.y)/2 == value)
    def MyFunction(self,v1,v2):
        return str(v1+v2)+" - "+str(self.x)
m = MyClass()
m2 = MyClass()
m2.x = 100
m.Test = m2.MyFunction
print (m.Test(1,2)) #3 - 100 , m.Test actually refers to m2.Test
print (m.MyFunction(1,2)) #3 - 10
