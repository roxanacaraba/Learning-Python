#citirea unui fisier exterior de tip txt folosind functia open, unde fisier-numele fisierului exterior si r=read
fisierulmeu = open("fisier", "r")
print(fisierulmeu.read())
fisierulmeu.close()