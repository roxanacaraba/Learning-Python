from collections import Counter
def functie(s,sub):
    total= Counter([s[i: i+len(sub)]for i in range(len(s))])
    return total[sub]
s ="pisica,caine,vaca,pisica"
sub="pisica"
print(functie(s,sub))
