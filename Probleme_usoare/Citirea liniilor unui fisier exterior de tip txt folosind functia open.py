#citirea  liniilor unui fisier exterior de tip txt folosind functia open, returnand un array, unde fisier-numele fisierului exterior si r=read
fisierulmeu = open("fisier", "r")
print(fisierulmeu.readlines())
fisierulmeu.close()