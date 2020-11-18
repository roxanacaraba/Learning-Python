a = input('Introdu primul numar: ')
b = input("Introdu al doilea numar: ")
def divizor(a,b):

    if a%b==0:
        return b
    for c in range(1,b):
        c+=1
        if a%c==0 and b%c==0:
           return c
x=str(divizor(int(a),int(b)))
print("cel mai mare dizivor comun este",x)




