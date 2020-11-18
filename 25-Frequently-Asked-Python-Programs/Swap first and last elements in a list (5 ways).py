#Varianta 1 cu o varianta temporara:
list=[12,35,9,56,24]

#size=len(list) #5
#temp=list[0]
#list[0]=list[size-1] # ultimul element are indexul 4
#list[size-1]=temp
#print("List after swapping var 1:", list)

#Varianta 2: # 0 e prima pozitie si -1 e ultima
#list[0],list[-1]=list[-1],list[0]
# stocam ultimul element in primul
# stocam primul element in ultimul
#print("List after swapping var 2", list)

#Varianta 3 utilizand tuple:
#get=(list[-1],list[0]) # se extrage ultimul si primul element intr-un tuple ( se numeste packing tehnica)
#list[0],list[-1]=get #adica e egal cu list[-1],list[0], si se procedeaza la fel ca la varianta a 2 a
#print("List after swapping var 3", list)

#Varianta 4 utilizant store operator
#start,*middle,end=list  # 12 va fi start, 54 va fi end, iar 35,9,56 vor fi in variabila *midle care e o sublista a listei.
#print(start)
#print(middle)
#print(end)
#list=[end,*middle,start]
#print("List after swapping var 4: " , list)

#Varianta 5 utilizand pop()

first=list.pop(0)  #12
last=list.pop(-1)  #24
list.insert(0,last)
list.insert(-1,first)
print("List after swapping var 5:", list)





