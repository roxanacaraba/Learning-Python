class Clasa:
    x=None
    def __str__(self):
        return str(self.x)
c=Clasa()
print(c)

class Number:
    a=2.5
    def __int__(self):
        return int(self.a)

c=Number()
value=int(c)
print(value)

class Number:
    def __init__(self, value):
        self.x=value
    def __eq__(self, other):
        return self.x +other.x== 0
n1=Number(-16)
n2=Number(16)
print(n1==n2)

class Number:
    def __init__(self,value):
        self.x=value
    def __contains__(self, item):
        return str(item) in str(self.x)
n=Number(358)
print(2 in n)
print(5 in n)