x = input("Introdu primul numar: ")
y = input("Introdu al doilea numar: ")
def computeGCD(x, y):
    while (y):
        aux = x % y
        x = y
        y = aux
    return x
z=str(computeGCD(int(x), int(y)))
print("cel mai mare divizor comun este: ",z)