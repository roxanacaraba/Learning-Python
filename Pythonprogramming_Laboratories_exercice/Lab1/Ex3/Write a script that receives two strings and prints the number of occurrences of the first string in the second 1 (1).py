s1="pisica, caine"
s2="pisica, caine, cal, vaca, pisica, caine"

def fun(s1,s2):
    if s2==s1:
        return 1
    else:
        import re
        result=len(re.findall(s1, s2))
        return result
print(fun(s1,s2))
