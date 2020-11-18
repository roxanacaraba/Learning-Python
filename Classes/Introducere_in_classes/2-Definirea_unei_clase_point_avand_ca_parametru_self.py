#For a function defined within a class to be a method of that class it has to have the first parameter self.
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
    def GetX(self):
        return self.x
p = Point()
print (p.GetX())