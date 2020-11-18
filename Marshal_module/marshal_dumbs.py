import marshal
d = {
    "a":[1,2,3],
    "b":100,

    "c":True
}
buffer = marshal.dumps(d)
open("serialization.marshal","wb").write(buffer)