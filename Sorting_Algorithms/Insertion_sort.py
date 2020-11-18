lista = [2,4,1,3]
"""
def Insertion_sort(lista):
    for i in range(1, len(lista)):
        for j in range(i-1, 0, -1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                break
"""
def insertion_sort(lista):
    index = range(1, len(lista))
    for i in index:
        value_to_sort=lista[i]
        while lista[i-1] > value_to_sort and i > 0:
            lista[i], lista[i - 1] = lista[i- 1], lista[i]
            i = i-1
    return lista
print(insertion_sort(lista))

