list=["iubire","ura","iubire","iubire","iubire"]
word="iubire"
n=3 #al catalea elem"iubire" vrem sa-l stergem
count=0
for i in range(0,len(list)-1):
    if (list[i]==word):
        count+=1
        if(count==n):
            del list[i]
print(list)