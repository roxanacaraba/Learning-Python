list=[15,6,7,10,12,20,10,28,10]

#varianta 1 folosind loop:
x=10      #elementul pt care vrem sa vedem de cate ori apare in lista
#count=0
#for elem in list:
#    if(elem==x):
#        count+=1 #variabila count stocheaza de cate ori apare 10 in lista
#print("{} apare de {} ori in lista".format(x,list.count))


#varianta 2 folosind count():
#print("{} apare de {} ori in lista".format(x,list.count(x)))

#varianta 3 folosind Counter():
from collections import Counter
dic=Counter(list)   # o sa rezulte un dictionar in care scrie elementul:de cate ori se repeta
print(dic)
print("{} apare de {} ori in lista".format(x,dic[x]))


