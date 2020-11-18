import zipfile
z = zipfile.ZipFile("archive.zip")
for i in z.infolist():
    print (i.filename,i.file_size,i.compress_size)
z.close()