import json
d = { "a":[1,2,3],
"b":100,
"c":True
}
s = json.dumps(d)
open("serialization.json","wt").write(s)
print (s)
