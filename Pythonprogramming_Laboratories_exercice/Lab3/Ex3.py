# Compare two dictionaries without using the operator "==" and return a list of differences as follows: (Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)
d1={"foo": "bar", "FOO": "BAR"}
d2={"foo": "bar", "f00": "b@r"}
set1=set(d1.items())
set2=set(d2.items())
print(set1- set2)
print(list(set1-set2))

