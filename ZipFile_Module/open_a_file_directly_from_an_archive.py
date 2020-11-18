import zipfile
z = zipfile.ZipFile("archive.zip")
f = z.open("sample_file.csv")
data = f.read()
f.close()
open("open_files.py", "wb").write(data)  # fisierul sample_file.csv va fi scris in noul fisier open_files.py
z.close()

#Method open from zipfile returns a file-like object. You can also specify a password:
#Format: ZipFile.open(name, mode='r', pwd=None)
