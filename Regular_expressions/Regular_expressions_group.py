import re
result = re.search(".*(.*)", "File size if 12345 bytes")
if result:
 print (result.group(0))
result = re.search(".*?(\d+)", "File size if 12345 bytes")
if result:
 print (result.group(0))

#sau
import re
result = re.search("\d+","Price is 123 USD")
if result:
 print (result.group(0))