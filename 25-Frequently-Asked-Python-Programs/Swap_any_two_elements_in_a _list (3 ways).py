list=[23,65,19,90]
#     0  1  2  3
#Varianta 1- Simple swap:
#vrem sa interschimbam elem de pe indexul 1(65) cu elem de pe indexul 3(90)
#pos1,pos2=1,3    #pos1 e list[1] si pos2 e list[3]
#list[pos1],list[pos2]=list[pos2],list[pos1]       #adica orice valoarea e in 1 o vom stoca in pos2, si orice valoare avem in 3, o vom stoca in pos1
#print("List after swapping var 1: " , list)

#Varianta 2 cu list.pop() building function:
pos1,pos2=1,3
#first_elem=list.pop(pos1)  #65 il stocam in first_elem --> rezulta ca lista va ramane 23,29,90
#second_elem=list.pop(pos2-1) #pe indexul 3 nu mai e nici un element deoarece au ramas doar 23,19,90 asa ca scadem 1 din pos2(3) ca sa ajungem la 90 care e pe index 2
#list.insert(pos1, second_elem)
#list.insert(pos2,first_elem)
#print("List after swapping var 2: ", list)

#Varianta 3 utilizand tuple:
get=(list[pos1],list[pos2])
list[pos2],list[pos1]=get
print("List after swapping var 3", list)









