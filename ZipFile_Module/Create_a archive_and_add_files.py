import zipfile
z = zipfile.ZipFile("new_archive.zip","w",zipfile.ZIP_DEFLATED)  #When creating an archive one can specify a desire compression: ZIP_DEFLATE, ZIP_STORED,
#ZIP_BZIP2 or ZIP_ZMA.
z.writestr("test.txt","un string...") #writestr method writes the content of a string into a zip file.
z.write("serialization.json")   #write methods add a file to the archive.
z.write("serialization.json", "/dir/a.json") #se adauga fisierul a.json in folderul dir
z.writestr("/dir/a.txt","alt string ...")    #se scrie :alt string..." in interiorul fisierului a.txt din folderul dir
z.close()

#vom extrage fisierele din noua arhiva pentru a le vedea:
z=zipfile.ZipFile("new_archive.zip") #toate fisierele din new_archive.zip vor fi extrase in folderul extracted_files
z.extractall("extracted_files_from_new_archive")
z.close()