#Defining a function within a class without having the first parameter self means that that function is a static function for that class

"""
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
    def GetY():
        return self.y
p = Point()
print (p.GetY()) # --> exercution error (GetY is static)
"""
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
    def GetY():  # Method must have a first parameter, usually called 'self'
        print("Test")
Point.GetY() # --> Will print "test" on the screen