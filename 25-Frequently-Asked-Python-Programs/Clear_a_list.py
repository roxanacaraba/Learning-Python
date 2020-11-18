list=[6,0,4,1]
print("List before clear:", list)

#Varianta 1 folosind clear()
#list.clear()
#print("List after clear:", list)

#Varianta 2 : initializes the list with no value
#list=[]
#print("List after clear:", list)

#Varianta 3 utilizand "*=0", aceasta metoda inlatura toate elementele si o face goala
#list *=0  #deletes the list
#print("List after clear:", list)

#Varianta 4
del list[1:3] # 0 4
print(list)
del list[:] # toata lista
print(list)







