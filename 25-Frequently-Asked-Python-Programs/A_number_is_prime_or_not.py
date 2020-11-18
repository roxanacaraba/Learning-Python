# Un număr prim este un număr natural, mai mare decât 1, care are exact doi divizori: numărul 1 și numărul în sine.
num=56
count=0
if num>1:
     for i in range(1,num+1):
         if(num%i)==0:
             count+=1
     if count==2:
         print("Numarul este prim")
     else:
         print("Numarul nu este prim")

