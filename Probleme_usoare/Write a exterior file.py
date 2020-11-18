# write intr-un fisier exterior deja existent in care sa se stearga ce era in el si sa se scrie noul element Miruna-8
fisierulmeu = open("fisier", "w")
fisierulmeu.write("\n Miruna-8")
fisierulmeu.close()


#write intr-un fisier exterior inexistent (adica creearea unui fisier nou in care sa se scrie elementul Miruna-8)
fisierulmeu = open("fisier1", "w")
fisierulmeu.write("\n Miruna-8")
fisierulmeu.close()