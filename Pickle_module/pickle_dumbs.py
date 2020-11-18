import pickle
d = {
    "a":[1,2,3],
    "b":100,
    "c":True
}
buffer = pickle.dumps(d) #buffer = pickle.dumps(d,0) (safety)
open("serialization.pickle","wb").write(buffer)