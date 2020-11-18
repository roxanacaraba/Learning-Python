# Write a function that receives as parameter a sorted list of tuples (last_name, first_name)
# like in ex.1 and a string representing a first_name.
# Check if the first_name is in the list.

# varianta I cu list.append:
lista=[("Popescu", "Maria"), ("Munteanu", "Bogdan"), ("Anton", "Cristi"), ("Zamfirescu", "Ion"), ("Lungu", "George")]
def funct(lista):
    string=input('Input first name: ')
    lista2=list()
    for i in lista:
        lista2.append(i[1])
    if string in lista2:
            print(True)
    else:
            print(False)
    return funct(lista)
print(funct(lista))

# Varianta II:
lista=[('Munteanu', 'Bogdan'), ('Anton', 'Cristi'), ('Lungu', 'George'), ('Zamfirescu', 'Ion'), ('Popescu', 'Maria')]
string="Georg"
def funct(lista,string):
    for elem in lista:
        if string==elem[1]:
            return True
    for elem in lista:  # sau pot inlocui liniile 40,41,42 cu return(False)
        if string != elem[1]:
            return False
print(funct(lista,string))
"""
compara(string1, string2)
    return 0 egale
    return -1 daca string 1 > string2
    return 1 altfel

def func1():
    return 1
def = definitie

def func2():
    val = func1()
    if val == 1:
        return "ceva"

    elif val == 9:
        return 1
"""

# Varianta III cu binary search:
lista = [('Munteanu', 'Bogdan'), ('Anton', 'Cristi'), ('Lungu', 'George'), ('Zamfirescu', 'Ion'), ('Popescu', 'Maria')]
def Compare_two_strings(string1, string2):
    if string1 == string2:
        return 0
    if string1 > string2:
        return -1
    if string1 < string2:
        return 1


def Binary_search(lista, low, high, first_name_entered):
    if high < low:
        return -1

    mid = (high+low) // 2
    result = Compare_two_strings(lista[mid][1], first_name_entered)
    if result == 0:
        return mid   #returneaza true daca vrei sa verifici daca exista in lista sau returneaza mid daca vrei sa afli indicele tuplelului in care se afla prenumele introdus
    elif result == -1:
        return Binary_search(lista, low, mid-1, first_name_entered)
    else:
        return Binary_search(lista, mid+1, high, first_name_entered)
print(Binary_search(lista, 0, len(lista)-1, "Bogdan"))
