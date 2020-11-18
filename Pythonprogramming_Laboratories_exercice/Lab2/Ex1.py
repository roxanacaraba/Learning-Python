# Sa se scrie o functie care sa returneze o lista cu primele n numere din sirul lui Fibonacci.
n =int(input("Enter how many Fibbonaci numbers do you want to get: "))
def fibbonacifunc(n):
    n1=0
    n2=1
    lista=list()
    if n == 0:
        print("You have chosen to display 0 Fibonacci numbers")
        lista.append(None)
    elif n == 1:
        print(n1)
        lista.append(n1)
    elif n == 2:
        print(n1)
        print(n2)
        lista.append(n1)
        lista.append(n2)
    else:
        print(n1)
        print(n2)
        lista.append(n1)
        lista.append(n2)
        for i in range(n-2):
            sum = n1+n2
            print(sum)
            n1 = n2
            n2 = sum
            lista.append(n1)
            lista.append(n2)
            lista.append(sum)
    return lista
fibbonacifunc(n)

