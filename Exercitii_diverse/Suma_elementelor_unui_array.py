list = {1, 2, 3, 4, 5}
n = len(list)


def sum(list):
    suma=0
    for element in list:
        suma += element
    return suma
a=sum(list)
print("suma elementelor este: ", a)

