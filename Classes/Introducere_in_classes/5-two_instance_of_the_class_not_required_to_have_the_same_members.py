#It is not required for two instances of the same class to have the same members.
# A class instance is more like a dictionary where each key represent either a member function or a data member

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
p1 = Point()
p2 = Point()
p1.z = 10
print (p1.x,p1.y,p1.z)
print(p1.x,p1.y,p2.z) #--> Error during runtine. “p2” does not have a data member “z” (only “p1” has a data member “z”)