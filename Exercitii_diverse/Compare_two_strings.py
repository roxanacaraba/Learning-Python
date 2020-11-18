string1 = "ana"
string2 = "ananas"
def compare(string1, string2):
    shortest_string_length = len(string1)
    if len(string2) < len(string1):
        shortest_string_length = len(string2)
    for i in range(shortest_string_length):
        if string1[i] > string2[i]:
            return 1
        elif string1[i] < string2[i]:
            return 2
    if len(string1) > len(string2):
        return 1
    elif len(string1) < len(string2):
            return 2
    return 0
print(compare(string1, string2))



