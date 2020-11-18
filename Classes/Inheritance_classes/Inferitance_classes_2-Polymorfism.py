#Polymorphism works in a similar way.
# In reality the inheritance is not necessary to accomplish polymorphism in Python
class Forma:
    def PrintName(self): pass
class Square(Forma):
    def PrintName(self): print("Square")
class Circle(Forma):
    def PrintName(self): print("Circle")
class Rectangle(Forma):
    def PrintName(self): print("Rectangle")
for form in [Square(),Circle(),Rectangle()]:
    form.PrintName()

class Square:
    def PrintName(self): print("Square")
class Circle:
    def PrintName(self): print("Circle")
class Rectangle:
    def PrintName(self): print("Rectangle")
for form in [Square(),Circle(),Rectangle()]:
    form.PrintName()
