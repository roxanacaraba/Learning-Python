s1="ABCABC"
s2="ABC"
m=len(s1)
n=len(s2)
def fun(s1,s2,m,n):
    if (m==0 and n==0):
        return 1
    if n==0:
        return 1
    if m==0:
        return 0
    else:
        return s1.count(s2)
print(fun(s1,s2,m,n))
