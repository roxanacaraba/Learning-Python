s="Hello"

#Varianta 1 cu for loop:
#count=0
#for i in s:
#   count+=1
#print(count)

#varianta a 2 a utilizand while loop si slicinf:
#count=0
#while s[count:]:  #slicing de la 0, apoi de la 1, apoi de la 2, pe masura ce creste count in valoare pana la finalul stringului
#    count+=1
#print(count)

#Varianta 3 utilizand len():
#print(len(s))

#Varianta 4 utilizand join si count:
random="X"
(random).join(s)  #X se adauga dupa fiecare elem din S : HXeXlXlXo
print((random).join(s).count(random)+1) #Numara cate X uri sunt in noul string si adauga unul pt ca dupa o nu s-a adaugat nici un X

