#We can write an equivalent representation of the functionality done by classes by using dictionaries:

class Point:
    def __init__(self):
       self.x = 0
       self.y = 0
p1 = Point()
p2 = Point()
p1.z = 10
print(p1.z)


#Dictionary representation:

def PointClass__init__(obj):
    obj["x"] = 0
    obj["y"] = 0
Point = { "__init__":PointClass__init__ }
p1 = dict(Point)    # -> Acest bloc e echivalentul lui p1 = Point() din primul cod.
p1["__init__"](p1)  # -> --- " ----
p2 = dict(Point)    #Iar acest bloc este echivalentul lui p2  =Point()
p2["__init__"](p2)  # -> --- " ----
p1["z"] = 10        #Aceasta linie e echivalenta lui p1.z=10
print(p1["x"],p1["y"], p1["z"])
