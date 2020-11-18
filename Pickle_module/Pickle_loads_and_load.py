import pickle
data = open("serialization.pickle","rb").read()
d = pickle.loads(data)
print (d)


#import pickle
#d = pickle.load(open("serialization.pickle","rb"))
#print (d)