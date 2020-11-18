s="te iubesc mult"
words=s.split(" ")
print(words)           #['te', 'iubesc', 'mult']
words=words[-1::-1]    #reverse string going back to first position by one
print(words)           #['mult', 'iubesc', 'te']
output=' '.join(words) #pt ca cuvintele sunt in lista mai sus si noi le vrem in string, accesam join() pt a le uni intr-un string
print(output)
