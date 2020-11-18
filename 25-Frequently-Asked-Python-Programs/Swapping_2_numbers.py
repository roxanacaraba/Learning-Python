num1=10
num2=20
print("valoarea primului numar inainte de swapping: ", num1)
print("valoarea celui de-al doilea numar inainte de swapping: ", num2)

# Prima abordare cu o variabila temporala:
temp=num1  #rezulta ca tem=10 pt ca num1=10
num1=num2  #rezulta ca num1=20 pt ca num2=20
num2=temp  #rezulta ca num2=10 pt ca temp=10

print("valoarea primului numar dupa swapping prin prima varianta: ", num1)
print("valoarea celui de-al doilea numar dupa swapping prin prima varianta: ", num2)

# A doua abordare:
num1,num2=num2,num1
print("valoarea primului numar dupa swapping prin a doua varianta: ", num1)
print("valoarea celui de-al doilea numar dupa swapping prin a doua varianta: ", num2)