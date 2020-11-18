lista=[1,2,3,4,5]

#Varianta 1 utilizand slicing technique:
#copie=lista[:]         #citeste toate elementele din lista daca nu specificam nimic in []
#print(copie)

#Varianta 2 utilizand extend() method:
#copie=[]              #Golim lista
#copie.extend(lista)    #Extendem copy cu lista noastra
#print(copie)

#Varianta 3 utilizand list() method:
#copie=list(lista)  # list() method va copia elementele din lista in copy
#print(copie)

#Varianta 4 utilizand copy() method:
#copie=lista.copy() #Copy() method va copia elementele din lista in copie
#print(copie)

#Varianta 5 utilizand list comprehension
copie=[i for i in lista]  #fiecare element din lista va fi stocat in i si apoi in copie
print(copie)

