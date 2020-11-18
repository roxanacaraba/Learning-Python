#A data member can also be defined directly in the class definition.
# However, if mutable object are used the behavior is different (similar in terms of behavior to a static variable)

class Point:
    x = 0
    y = 0
p1 = Point()
p2 = Point()
p1.x = 10
p2.x = 20
print (p1.x,p2.x)


class Point:
    numbers = [1,2,3]
    def AddNumber(self,n):
        self.numbers += [n]
p1 = Point()
p2 = Point()
p1.AddNumber(4)
p2.AddNumber(5)
print (p1.numbers) #[1, 2, 3, 4, 5]
print (p2.numbers) #[1, 2, 3, 4, 5]

#To avoid problems with mutable objects it is better to defined them in a constructor (__init__) function
class Point:
    def __init__(self):
       self.numbers = [1,2,3]
    def AddNumber(self,n):
       self.numbers += [n]
p1 = Point()
p2 = Point()
p1.AddNumber(4)
p2.AddNumber(5)
print (p1.numbers) #[1, 2, 3, 4]
print (p2.numbers) #[1, 2, 3, 5]

