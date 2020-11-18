#Python defines a special set of functions that can be use do add additional properties to a class.
#Just like the initialization function (__init__) , these functions start and end with “__”

#__repr__, __str__                                Called when the object needs to be converted into string
#__lt__, __le__, __eq__, __ne__, __gt__, __ge__   Operators used to compare instances of the same class.
#__bool__                                         To evaluate the truth value of an object (instance of a class)
#__getattr__, __getattribute__                    For attribute look-ups
#__setattr__, __delattr__,__set__, __get__        For attribute operations
#__len__, __del__,                                For len / del operators
#__setitem__, __getitem__, __contains__,          Iterator operators
# _reversed__, __iter__, __next__

#Converting a class to a string: using __str__ si __repr__
class Test:
    x=10
class Test2:
    x=10
    def __str__(self):
        return "Test2 with X=" + str(self.x)
t=Test()
t2=Test2()
print(t, ":", str(t))
print(t2, ":", str(t2))

#Converting to an integer value:
class Test:
    x=10
class Test2:
    x=10
    def __int__(self):
        return self.x
t=Test()
t2=Test2()
Value=int(t2)
print(Value)

#Iterationg through a class instance:
class CarList:
    cars = ["Dacia","BMW","Toyota"]
    def __iter__(self):
       self.pos = -1
       return self
    def __next__(self):
       self.pos += 1
       if self.pos==len(self.cars):
           raise StopIteration
       return self.cars[self.pos]
c= CarList()
for i in c:
    print (i)

#Using class operators.

# ___eq__ e acelasi cu ==
class Number:
    def __init__(self, value):
        self.x = value
    def __eq__(self, obj):
        return self.x+obj.x == 0
n1 = Number(-5)
n2 = Number(5)
n3 = Number(6)
print (n1==n2)
print (n1==n3)

#Overwriting the "in" operators (__contains__)
class Number:
    def __init__(self, value):
        self.x=value
    def __contains__(self,value):
        return str(value) in str(self.x)
n=Number(123)
print(1 in n)
print(15 in n)
print(23 in n)

#Overwriting the "len" operator:
class Number:
    def __init__(self, value):
        self.x=value
    def __len__(self):
        return len(str(self.x))
n1=Number(113)
n2=Number(9999999)
n3=Number(1)
print(len(n1), len(n2), len(n3))


#Building your own dictionary (overwrite __setitem__ si __getitem__)
class dict:
    def __init__(self):
        self.data=[]
    def __setitem__(self, key, value):
        self.data+=[(key, str(value))]
    def __getitem__(self,key):
        for i in self.data:
            if i[0]==key:
                return i[1]
d=dict()
d["test"]="python"
d["numar"]=123
print(d["test"], d["numar"])


#Building a bit set (overloading operator[])
class BitSet:
    def __init__(self):
        self.value = 0
    def __setitem__(self,index,value):
        if value:
            self.value |= (1 << (index & 31))
        else:
            self.value -= (self.value & (1 << (index & 31)))
    def __getitem__(self,index):
        return (self.value & (1 << (index & 31)))!=0
b = BitSet()
b[0] = True
b[2] = True
b[4] = True
for i in range(0,8):
    print("Bit ",i," is ",b[i])

