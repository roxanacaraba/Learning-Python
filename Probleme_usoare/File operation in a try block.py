#returneaza liniile fisierului folosind un bloc try5
try:
    f = open("fisier")
    for line in f:
        print(line.strip())
    f.close()
except:
    print("Unable to open file fisier")