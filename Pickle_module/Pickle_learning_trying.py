import pickle
d={
    "Food type": {
    "Romanian": ["Ciorba", "Mamaliga & Sarmale", "Tocanita"],
    "Italian" : ["Paste" , "Pizza", "Rissoto"],
    "Fast Food": ["Burger", "Fries", "Shaorma", "Kebab"],
    "Price":[
        {"Price for Romanian food": 25,
         "Price for Italian food": [
             {
                 "Paste":19,
                 "Pizza":27,
                 "Rissoto":13}
         ],
         "Price for fast food":10
             }
         ]
    }

    }
buffer = pickle.dumps(d)
open("serialization_try.pickle","wb").write(buffer)