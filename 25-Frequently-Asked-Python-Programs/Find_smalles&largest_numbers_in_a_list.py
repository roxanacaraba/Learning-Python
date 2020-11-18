list=[20,100,20,1,10]

#Prima varianta: sorteam elementele ascendent in lista apoi extragem primul elem=cel mai mic si ultimul elem=cel mai mare
#list.sort()  #sorteaza elementele
#print("Cel mai mic numar este: ", list[0])
#print("Cel mai mare numar este: ", list[-1])

#Varianta a 2 a: utilizand min() si max()
print("Cel mai mic numar este: ", min(list))
print("Cel mai mare numar este: ", max(list))