arr=[30,20,3,54,15]
#Logical aproach:

#Gasirea max:
max=arr[0] # consideram elementul de pe indicele 0 ca fiind max si il comparam cu fiecare element ramas, daca elementul cu indice 0 e mai mic ca celalalt element cu care e comparat, se face swap
n=len(arr)
for i in range(1,n):
    if arr[i]>max:
        max=arr[i]
print("Maximum elemnt is: " , max)

#Gasirea min:
arr=[30,20,3,54,15]
min=arr[0]
n=len(arr)
for i in range(1,n):
    if arr[i]<min:    #daca arr[i] mai mic ca min stabilit mai sus, adica ca elem de pe indicele 0
        min=arr[i]    # atunci arr[i] va deveni noul min
print("Minimum element is: " ,min)