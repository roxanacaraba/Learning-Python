fisierulmeu = open("fisier", "r")
for persoane in fisierulmeu.readlines():
    print(persoane)
fisierulmeu.close()