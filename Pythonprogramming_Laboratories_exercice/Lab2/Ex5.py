# Sa se scrie o functie care primeste ca parametru o lista x, si un numar k.
# Sa se returneze o lista cu tuple care sa reprezinte combinari de len(x) luate cate k din lista x.
# Exemplu: pentru lista x = [1,2,3,4] si k = 3 se va returna [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)].
# cod care foloseste itertools:
"""from itertools import combinations
def funct():
    x = list(map(int, input("Introdu lista : ").strip().split()))
    k = int(input("Introdu numarul: "))
    comb = combinations(x, k)
    lista= list(comb)
    return(lista)
print(funct())

# Cod care nu da outputul bun:
x = list(map(int, input("Introdu lista : ").strip().split()))
print(x)
k = int(input("Introdu numarul: "))
print(k)
def combfunct(x,k):
    if k == 0:
        return [[]]
    l=list()
    for i in range(0, len(x)):
        m=x[i]
        X=x[i+1:]
        for p in combfunct(X,k-1):
            l.append([m]+p)
            return l

print(combfunct(x,k))

# Cod care da toate combinarile posibile:
x = list(map(int, input("Introdu lista : ").strip().split()))
k = int(input("Introdu numarul: "))
def comb():
    lista= list((i,j,n) for i in x for j in x for n in x)
    return(lista)
print(comb())
"""
# Cod care utilizeaza backtracking:
x = list(map(int, input("Introdu lista : ").strip().split()))
k = int(input("Introdu numarul: "))


def backtracking(x, k):
    list1 = list()
    list2= list()
    for i in x:
        list1.append(i)
        if len(list1) == k:
            list2.append(list1)
        if len(list2) == len(x):
            return backtracking(list2, k)

print(backtracking(x, k))



