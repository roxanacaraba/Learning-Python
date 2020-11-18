# Write a function that receives a string as a parameter and returns a dictionary in which the keys are the characters in the character string and the values are the number of occurrences of that character in the given text.
# Example: For string "Ana has apples." given as a parameter the function will return the dictionary: {'A': 1, '': 2, 'n': 1, 'a': 2, 'r': 2, '.': 1}.

# varianta 1
string=input("Input your string: ")
def funct(string):
    dict={}
    for i in string:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]= 1
    return dict
print(funct(string))

# varianta 2
from collections import Counter
def counter():
    string=input("Input your string :")
    result=Counter(string)
    return result
print(counter())