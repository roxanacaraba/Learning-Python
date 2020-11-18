# Write a function that receives as parameters two lists a and b and returns a tuple of sets containing:
# (a intersected with b, a reunited with b, a - b, b - a)
a = list(map(int, input("Input first list : ").strip().split()))
b = list(map(int, input("Input second list : ").strip().split()))

def funct(a,b):
    # intersection:
    list3 = [value for value in a if value in b]
    x=set(list3)
    # union:
    list3 = a + b
    z= set(list3)
    # a-b:
    list3 = [i for i in a + b if i not in b or i not in a]
    y1=set(list3)
    # b-a:
    list3 = [i for i in b + a if i not in a or i not in b]
    y2 = set(list3)
    t=(x,z,y1,y2)
    return t
print(funct(a,b))

# sau folosind operatii cu seturi
def funct(a,b):
    A = set(a)
    B = set(b)
    u = A.union(B)
    i = A.intersection(B)
    dif1 = A.difference(B)
    dif2 = B.difference(A)
    t=( i, u, dif1, dif2)
    return t
print(funct(a,b))