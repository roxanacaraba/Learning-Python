import hashlib
m = hashlib.md5()
m.update(b"Today")
m.update(b" I'm having")
m.update(b" a Python ")
m.update(b"course")
print (m.hexdigest())
import hashlib
print (hashlib.md5(b"Today I'm having a Python course").hexdigest())
print (hashlib.md5(b"Today I'm having a Python course").digest())

#Hashes are often use on files (to associate the content of a file to a specific hash)
import hashlib
def GetFileSHA1(fisierul):
    fisierul="fisier.txt"
    m = hashlib.sha1()
    m.update(open(fisierul,"rb").read())
    return m.hexdigest()
print (GetFileSHA1("fisier.txt"))

#The correct way to do this (having a support for large files is as follows):
import hashlib
def GetFileSHA1(filePath):
    try:
        m = hashlib.sha1()
        fisierul ="fisier.txt"
        f = open(fisierul,"rb")
        while True:
            data = f.read(4096)
            if len(data)==0:
                break
            m.update(data)
        f.close()
        return m.hexdigest()
    except:
        return ""
print(GetFileSHA1("fisier.txt"))