#Just like normal variables in Python, data members can also have their type changed dynamically.
class MyClass:
    x = 10
    y = 20
m = MyClass()
print (m.x,"=>",type(m.x))
m.x = "a string"
print (m.x,"=>",type(m.x))

#The same can be applied for class methods – however in this case there are some restrictions related to the self keyword.
class MyClass:
    x = 10
    y = 20
    def Test(self,value):
        return ((self.x+self.y)/2 == value)
    def MyFunction(self,v1,v2):
        return str(v1+v2)+" - "+str(self.x)+","+str(self.y)
m = MyClass()
print (m.Test(15),m.Test(16))  # se calculeaza daca x+y/2 este egal cu 15, respectiv 16
m.Test = m.MyFunction          #daca punem in loc de "m" "MyClass" va aparea: Runtime error because “MyFunction” is a method that needs to be bound to an object instance !
print (m.Test(1,2))            #se calculeaza 1+2 - x,y

#se poate folosi in schimbul lui m.Test = m.MyFunction :
m.Test=MyClass().MyFunction

#sau:
m = MyClass()
m2 = MyClass() #adaugam o variabila m2
print (m.Test(15),m.Test(16))
m.Test = m2.MyFunction
print (m.Test(1,2))
