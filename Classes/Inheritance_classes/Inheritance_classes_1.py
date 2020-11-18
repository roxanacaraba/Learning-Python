#Python classes supports both simple and multiple inheritance.

#class <name>(Base):
#<statement1>
#…
#<statementn>

#class <name>(Base1,Base2,… Basem):
#<statement1>
#…
#<statementn>

#Python has two keywords (issubclass and isinstance) that can be used to check if an object is a subclass of an instance of a specific type.
class Base:
    x = 10
class Derived(Base):
    y = 20
d = Derived()
print ("d.X = ",d.x)
print ("d.Y = ",d.y)
print ("Instance of Derived:",isinstance(d,Derived))
print ("Instance of Base:",isinstance(d,Base))
print ("Derived is a subclass of Base:",issubclass(Derived,Base))
print ("Base is a subclass of Derived:",issubclass(Base,Derived))

#Inheritances does not assume that the __init__ function is automatically called for the base when the derived object is created.
#class Base:
#    def __init__(self):
#       self.x = 10
#class Derived(Base):
#    def __init__(self):
#        self.y = 20
#d = Derived()
#print ("d.X = ",d.x) #Execution error – d.X does not exists because base.__init__ was never called
#print ("d.Y = ",d.y)

class Base:
    def __init__(self):
        self.x = 10
class Derived(Base):
    def __init__(self):
        Base. __init__(self) #In Python 3 you can also write super().__init__()
        self.y = 20
d = Derived()
print ("d.X = ",d.x) #10
print ("d.Y = ",d.y) #20

#Inheriting from a class will overwrite all base class members (methods or data members).
class Base:
    def Print(self):
        print("Base class")
class Derived(Base):
    def Print(self):
        print("Derived class")
d = Derived()
d.Print()  #Derived class

class Base:
    def Print(self,value):
        print("Base class",value)
class Derived(Base):
    def Print(self):
        print("Derived class")
d = Derived()
d.Print()
d.Print(100)  #Print function from Base class was completely overwritten by Print function from the derived class. The code will produce a runtime error.

#Inheriting from a class will overwrite all base class members (methods or data members).
#In this case member “x” from Base class will be overwritten by member “x” from the derived class.
class Base:
    x = 10
class Derived(Base):
    x = 20
d = Derived()
print (d.x) #20
