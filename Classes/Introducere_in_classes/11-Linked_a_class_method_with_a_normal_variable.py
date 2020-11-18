#Similarly a class method can be associated (linked) to a normal variable and used as such.
# It will be able to use the self and it will be affected if self members are changed.
class MyClass:
     x = 10
     def MyFunction(self,v1,v2):
         return str(v1+v2)+" – self.x:"+str(self.x)
m = MyClass()
fnc = m.MyFunction
print (fnc(15,35))
m.x = 123
print (fnc(15,35))