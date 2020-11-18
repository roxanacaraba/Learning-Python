#import zipfile
#z = zipfile.ZipFile("archive.zip")
#z.extract("sample_file.csv", "ZipFile_Module")
#z.close()

#to extract all files:
import zipfile
z=zipfile.ZipFile("archive.zip") #toate fisierele din archive.zip vor fi extrase in folderul extracted_files
z.extractall(("extracted_files"))
z.close()

