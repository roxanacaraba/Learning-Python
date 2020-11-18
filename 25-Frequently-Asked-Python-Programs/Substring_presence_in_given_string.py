#The find method(0 finds the first occurence of the specified value.
#The find method(0 returns -1 if the value is not found.

s="welcome to python programming"
sub="python"
print(s.find(sub)) #se printeaza indexul de la care incepe cuvantul python (11)

if(s.find(sub))==1:
    print("Not found")
else:
    print("Found")