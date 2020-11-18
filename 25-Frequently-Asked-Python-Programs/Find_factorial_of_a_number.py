#factorialul lui 5 este : 5!=1*2*3*4*5=120
factorial=1
num=10
#Prima abordare:
#if num<0:
   # print("Nu exista factorial pentru numere negative")
#elif num==0:
   # print("Factorialul lui 0 este 1")
#else:
   # for i in range(1,num+1):
       # factorial=factorial * i
    #print("Factorialul lui",num, "este", factorial)

#A doua abordare cu recursive function:
# 5* (5-1) * (4-1) * (3-1)* (2-1)=5!
#def factorial(n):
   # if(n==0 or n==1):
       # return 1
    #else:
      #  return n * factorial(n-1) # 5*4*3*2*1 se apeleaza functia factorial din nou si din nou pana se epuizeaza n-1
#num=5
#print("factorialul lui", num, "este ", factorial(num))

#A treia abordare mai scurta :
def factorial(n):
    #Ternary operator
    return 1 if (n==1 or n==0) else n*factorial(n-1)
num=13
print("factorialul lui", num, "este ", factorial(num))
