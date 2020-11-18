# Fie un tuplu (x,y) reprezentarea unui punct intr-un sistem cartezian.
# Sa se scrie o functie care primeste ca parametru o lista de puncte si
# returneaza o lista de tuple (a,b,c) unice care reprezinta dreptele unice determinate de acele puncte ( (a,b,c) corespunde dreptei ax + by + c = 0).

# Acest cod returneaza o lista cu tuple doar pt primele 2 puncte:
lista=list([(x,y) for x in range(0, 6, 2) for y in range(0, 7, 3)])
def funct(lista):
    lst = list()
    for i in range(len(lista)-1):
        P = lista[i]
        Q = lista[i+1]
        a = Q[1] - P[1]
        b = P[0] - Q[0]
        c = a * (P[0]) + b * (P[1])
        #t=(a,b,c)
        #l=list()
        #l.append(a)
        #l.append(b)
        #l.append(c)
        #t= tuple(l)
        #lst.append(t)
        lst.append((a,b,c))
    return(lst)
print(funct(lista))







