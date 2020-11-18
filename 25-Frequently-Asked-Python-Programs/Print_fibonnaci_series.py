# un numar fibonacci este un numar alcatuit din suma celor 2 numere precedente lui.
# 0   1   1    2   3   5   8   13   21  34
# n1 n2
#    n1  n2
#        n1  n2
#                 n1  n2
# n1 si n2 se muta la fiecare iteratie

n1=0
n2=1
print(n1)
print(n2)
for i in range(2,10):
    sum=n1+n2 # 0+1
    print(sum) #1
    n1=n2     # n1 ia valoarea lui n2 si devide 1, apoi la urm iteratie n1 ia valoarea lui n2 si devine 1, apoi devine 2 , apoi devine 3
    n2=sum    # n2 ia valoarea lui sum si devine 1 , apoi la urm iteratie n2 ia valoarea lui sum si devine 2, apoi devine 3, apoi devine 5


