#You can also delete a member of a class instance by using the keyword del
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
p = Point()
print (p.x,p.y)
p.x = 10
print (p.x,p.y)
del p.x
print (p.x,p.y) #--> “x” is no longer a member of p. Code will produce a runtine error.