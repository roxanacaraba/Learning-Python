#class <name>:
#<statement1>
#…
#<statementn>
#Where statement is usually a declaration of a method or data member

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
p = Point()
print (p.x,p.y)
