#Varianta 1 utilizand loop

list=[1,6,3,5,3,4]
e=4
#flag=0
#for i in list:
 #   if(i==e):   #daca nu se potrivesc va lua din nou un nou i si il va compara cu e pana cand se va gasi un i care sa fie=e
  #      print("Element found")
   #     flag=1  #daca se gaseste un i=e variabila flag devine 1
    #    break   # se opreste cautarea
#if (flag==0):
   # print("Element not found")

#Varianta 2 utilizand in operator:
if (e in list):
    print("Element found")
else:
    print("Element not found")