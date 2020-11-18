#self object is assign during the construction of an object.
# This means that a function can be defined outside the class and used within the class if it is set during the construction phase.

def MyFunction(self,v1,v2):
    return str(v1+v2)+" - X = "+str(self.x)
class MyClass:
    x = 10
    Test = MyFunction
m = MyClass()
m2 = MyClass()
m2.x = 15
print (m.Test(1,2))
print (m2.Test(10,20))

#This type of assignment can not be done within the constructor method (__init__), it must be done through direct declaration in the class body.
def MyFunction(self,v1,v2):
    return str(v1+v2)+" - X = "+str(self.x)
class MyClass:
    x = 10
    def __init__(self):
        self.Test = MyFunction
m = MyClass()
m2 = MyClass()
m2.x = 15
print (m.Test(1,2)) #The code will produce a runtime error because MyFunction is not bound to any self at this point
print (m2.Test(10,20))


#The same error will appear if we try to link a method from a class using it’s instance with a nonclass function.
def MyFunction(self,v1,v2):
    return str(v1+v2)+" - X = "+str(self.x)
class MyClass:
    x = 10
m = MyClass()
m2.Test = MyFunction
print (m.Test(1,2)) #The code will produce a runtime error because MyFunction is not bound to any self at this point