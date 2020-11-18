
#import json
#data = open("serialization.json","rt").read()
#d = json.loads(data)
#print (d)


import json
d = json.load(open("serialization.json","rt"))
print (d)