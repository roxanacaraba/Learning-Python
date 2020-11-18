#o random.random()  a random float number between 0 and 1
#o random.randint(min,max)  a random integer number between [min … max]
#o random.choice(list)  selects a random element from a list
#o random.shuffle(list)  shuffles the list
#o random.sample(list,count)  creates another list from the current one containing count elements

import random
print(random.random())
print(random.randint(1,9))
list=[1,6,3,19,25,42,89]
print(random.choice(list))
print(random.sample(list,4))
random.shuffle(list)
print(list)