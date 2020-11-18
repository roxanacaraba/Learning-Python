#In case of multiple inheritance, Python derives from the right most class to the left most class from the inheritance list.
class BaseA:
    def MyFunction(self):
        print ("Base A")
class BaseB:
    def MyFunction(self):
        print ("Base B")
class Derived(BaseA, BaseB): #First MyFunction from BaseB is added to Derived class
    pass                     #Then MyFunction from class BaseA will overwrite MyFunction from BaseB
d = Derived()
d.MyFunction()  #Base A

#If we reverse the order (BaseB will be first and BaseA wil be the last one), MyFunction will print “Base B” instead of “Base A”
class BaseA:
    def MyFunction(self):
        print ("Base A")
class BaseB:
    def MyFunction(self):
        print ("Base B")
class Derived(BaseB, BaseA):
    pass
d = Derived()
d.MyFunction()
