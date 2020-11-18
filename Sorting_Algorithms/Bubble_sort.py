lista = [5, 8, 2, 9, 0, 7, 3, 6]


def Bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
Bubble_sort(lista)
print(lista)

def bubble_sort(array):
    ok = False
    while ok == False:
        ok = True
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                ok = False
                # switch
                aux = array[i]
                array[i] = array[i+1]
                array[i+1] = aux
bubble_sort(lista)
print(lista)



