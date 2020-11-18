list=[10,20,4,45,99]

#Varianta 1 prin sortare
#list.sort()
#print(list)
#print("2nd largest number in list is:", list[-2])


#Varianta 2
new_list=set(list) #new_list contine aceleasi elemente ca list doar ca e de tip set, nu lista
new_list.remove(max(new_list))  #inlatura maximul din lista ca sa ramanem cu [10,20,4,45]
print(max(new_list))            #afiseaza maximul din new_list, care este al doilea max din lista initiala
