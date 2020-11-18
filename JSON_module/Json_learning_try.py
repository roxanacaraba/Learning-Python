import json
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

#s=json.dumps(d, indent=4)
#open("Serialization_trying.json", "wt", ).write(s)
#print(s)


d=open("Serialization_trying.json", "rt").read()
r=json.loads(d)
print(r)


#r=json.load(open("Serialization_trying.json", "rt"))
#print(r)