#  Write a function that receives as a parameter a set and returns a tuple (a, b), representing the number of unique elements in the set, and b representing the number of duplicate elements in the set.
set=(input("Input your set: "))
def funct(set):
    t=tuple()
    dict={}
    for i in set:
        if i in dict:
            dict[i]+= 1
        else:
            dict[i] = 1
        a=0
        b=0
        for i in dict.values():
            if i == 1:
                a+=1
        for i in  dict.values():
            if i > 1:
                b+=1
        t=(a,b)
    return t
print(funct(set))





