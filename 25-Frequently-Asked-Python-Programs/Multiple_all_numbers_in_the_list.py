list=[3,2,4]

#varianta 1: Traversal
#result=1
#for x in list:
#    result=result * x  #x reprezinta fiecare element din lista, deci initial se inmulteste 1(result) cu 3, dupa cu 2,dupa cu 4
#print(result)

#Varianta 2 utilizand numpy.prod()    - trebuie sa instalezi numpy package
import numpy
result=numpy.prod(list)  #se vor inmulti elementele listei si rezultatul se va stoca in result
print(result)



