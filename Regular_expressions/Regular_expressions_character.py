import re
s="maine o sa ploua si vor cadea 10-20 sau 30,60 de litri de AAA apa"
#cand folosim re.match se opreste cautarea dupa primul match
#cand folosim re.findall se afiseaza toate match urile
#utilizarea . inseamna ca se cauta toate caracterele in cu exceptia unei noi linii

result=re.match(".", s)
print(result)         #arata primul caracter

result=re.findall(".", s)
print(result)                              #arata toate caracterele inclusiv whitespace

#utilizarea ^ inseamna ca se verifica match urile de la inceputul string-ului
# # utilizarea $ inseamnca ca se verifica match urile de la finalul stringului
# \w inseamna ca se verifica caractere a-z , A-Z, 0-9 si _
#\w+ inseamna ca se verifica cuvintele

result=re.match("^\w",s)
print(result)                              #gaseste primul caracter litera, cifra sau _

result=re.match("^\w+",s)
print(result)                              #gaseste primul cuvant

result=re.findall("\w", s)
print(result)                              #gaseste toate caracterele litere sau cifre sau _

result=re.findall("\w+", s)
print(result)                              #gaseste toate cuvintele

result=re.search("\w+$",s)                 #daca voi folosi match in loc de search se va afisa None pt ca match verifica de la inceputul string-ului
print(result)                              #verifica daca sfarsitul stringului se potriveste cu patternul

result=re.findall("\w+$", s)
print(result)                              #gaseste ultimul cuvant din string

# *         Causes the resulting RE to match 0 or more repetitions of the preceding RE, as many repetitions as are possible.
# ab* will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.

# +         Causes the resulting RE to match 1 or more repetitions of the preceding RE.
# ab+ will match ‘a’ followed by any non-zero number of ‘b’s; it will not match just ‘a’.

# ?         Causes the resulting RE to match 0 or 1 repetitions of the preceding RE.
# ab? will match either ‘a’ or ‘ab’

# *?, +?, ??    The '*', '+', and '?' qualifiers are all greedy;
# they match as much text as possible.
# Sometimes this behaviour isn’t desired;
# if the RE <.*> is matched against '<a> b <c>', it will match the entire string, and not just '<a>'.
# Adding ? after the qualifier makes it perform the match in non-greedy or minimal fashion; as few characters as possible will be matched.
# Using the RE <.*?> will match only '<a>'.

result=re.search("A{3}",s)               # {m} Specifies that exactly m copies of the previous RE should be matched; fewer matches cause the entire RE not to match.
print(result)                            # For example, a{6} will match exactly six 'a' characters, but not five.

result=re.search("A{3,}",s)
print(result)
# {m,n}   Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as many repetitions as possible.
# For example, a{3,5} will match from 3 to 5 'a' characters. Omitting m specifies a lower bound of zero, and omitting n specifies an infinite upper bound.
# As an example, a{4,}b will match 'aaaab' or a thousand 'a' characters followed by a 'b', but not 'aaab'.

# {m,n}?
# Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as few repetitions as possible.
# This is the non-greedy version of the previous qualifier.
# For example, on the 6-character string 'aaaaaa', a{3,5} will match 5 'a' characters, while a{3,5}? will only match 3 characters.

# utilizarea |
#A|B, where A and B can be arbitrary REs, creates a regular expression that will match either A or B.
#once A matches, B will not be tested further, even if it would produce a longer overall match.

# utilizarea ()
#Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group;
#To match the literals '(' or ')', use \( or \), or enclose them inside a character class: [(], [)].

#utilizarea \w
#Matches Unicode word characters; this includes most characters that can be part of a word in any language, as well as numbers and the underscore.
# If the ASCII flag is used, only [a-zA-Z0-9_] is matched.
result=re.match("[a-zA-Z0-9_]",s)
print(result)                              #gaseste primul caracter word

# \W
# Matches any character which is not a word character. This is the opposite of \w.
# If the ASCII flag is used this becomes the equivalent of [^a-zA-Z0-9_].
result=re.match("[^a-zA-Z0-9_]",s)
print(result)
