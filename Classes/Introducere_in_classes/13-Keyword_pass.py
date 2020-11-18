#A class can be used like a container of data (a sort of name dictionary).
# It’s closest resemblance is to a struct in C-like languages.
# For this an empty class need to be create (using keyword pass)
class Point:
    pass
p = Point()
p.x = 100
p.y = 200
p_3d = Point()
p_3d.x = 10
p_3d.y = 20
p_3d.z = 30
print ("P = ",p.x,p.y)
print ("3D= ",p_3d.x,p_3d.y,p_3d.z)