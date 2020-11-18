# Write a function that receives as parameter a list of tuples (last_name, first_name) and returns the list sorted by first_name.
# Varianta 1:
def funct(i):
    return i[1]
lista=[("Popescu", "Maria"), ("Munteanu", "Bogdan"), ("Anton", "Cristi"), ("Zamfirescu", "Ion"), ("Lungu", "George")]
lista.sort(key= funct)
print(lista)

"""# Varianta 2:
lista=[("Popescu", "Maria"), ("Munteanu", "Bogdan"), ("Anton", "Cristi"), ("Zamfirescu", "Ion"), ("Lungu", "George")]
def funct(lista):
    for i in lista:
        lista.sort(key=lambda i : i[1])
    return lista
print(funct(lista))"""