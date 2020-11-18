#import marshal
#data = open("serialization.marshal","rb").read()
#d = marshal.loads(data)
#print (d)

import marshal
d = marshal.load(open("serialization.marshal","rb"))
print (d)