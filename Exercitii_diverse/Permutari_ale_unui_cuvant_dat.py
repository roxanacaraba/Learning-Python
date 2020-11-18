"""from itertools import permutations

word = input("Input your word: ")
def perm(word):
    p = permutations(word)
    lista= list(p)
    return lista
print(perm(word))
"""
def perm(remaining, string_gol=""):
    if len(remaining)==0:
        print(string_gol)
    for i in range(len(remaining)):
        new_string_gol=string_gol + remaining[i]
        new_remaining=remaining[0:i] + remaining[i+1:]
        perm(new_remaining,new_string_gol)
word = input("Input your word: ")
print(perm(word))
