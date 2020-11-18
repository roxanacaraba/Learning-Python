# Sa se scrie o functie care primeste ca parametri doua liste a si b si returneaza: (a intersectat cu b, a reunit cu b, a - b, b - a)
list1 = list(map(int, input("Input first list : ").strip().split()))
list2 = list(map(int, input("Input second list : ").strip().split()))


def intersection(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3
x=intersection(list1, list2)
print("Intersectia celor 2 liste este : ", x)


def difference(list1, list2):
    list3 = [i for i in list1 + list2 if i not in list1 or i not in list2]
    return list3

x=difference(list1, list2)
print("Diferente dintre prima lista si a doua lista este : ", x)

x=difference(list2, list1)
print("Diferenta dintre a doua lista si prima lista este: ", x)


def union(list1, list2):
    list3 = list1 + list2
    return sorted(list3)

x=union(list1,list2)
print("Reuniunea dintre cele doua liste este: ", x)