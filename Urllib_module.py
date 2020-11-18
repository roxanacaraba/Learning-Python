import urllib
import re
from urllib import request
urlManagement = 'http://www.info.uaic.ro/bin/Structure/Management'
r = re.compile(b"Dean.*<a href=\"[^\"]+\">([A-Za-z\s]+)")
try:
    response = urllib.request.urlopen(urlManagement).read()
    obj = r.search(response)
    if obj:
        print ("Our dean is : ",obj.group(1))
except Exception as e:
    print ("Error -> ",e)