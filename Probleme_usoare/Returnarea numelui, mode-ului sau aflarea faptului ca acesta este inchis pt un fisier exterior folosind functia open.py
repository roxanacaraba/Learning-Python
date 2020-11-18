f=open("fisier", "rb")
print("Numele fisierului:", f.name)

#sau mode-ul:
print("File open mode: ", f.mode)

#sau returneza daca fisierul e inchis:
print("Este inchis?", f.closed)