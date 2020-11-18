s1="pisica, caine"
s2="pisica, caine, cal, vaca, pisica, caine"
def fun(s1,s2):
    if s1==s2:
        return(1)
    else:
        return s2.count(s1)
print(fun(s1,s2))