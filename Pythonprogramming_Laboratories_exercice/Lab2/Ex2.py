# Sa se scrie o functie care primeste o lista de numere si returneaza o lista cu numerele prime care se gasesc in ea.


def listfunction():
    numbers = list(map(int, input("Input your numbers : ").strip().split()))  # how to input list of integers in python
    lista = list()
    for num in numbers:
        count = 0
        if num > 1:
            for i in range(1, num+1):
                if (num % i) == 0:
                    count += 1
            if count == 2:
                lista.append(num)
    return lista


x = listfunction()
print(x)
