string="Astazi este o zi minunata de 15 septembrie"
import re

#re.compile

# pt gasirea primului cuvant din string folosim match
prog = re.compile("\w+")
result = prog.match(string)
print(result)
#sau pt gasirea tuturor cuvintelor folosim findall
prog = re.compile("\w+")
result = prog.findall(string)
print(result)
 #este echivalent cu:
result = re.match("\w+", string)
print(result)
#sau
result = re.findall("\w+",string)
print(result)

#sau
import re
r=re.compile("[A-Z]{3}")
if r.match("ABD"):
    print("Match")

#re.search pt a scana stringul si a returna primul cuvant
result = re.search("\w+", string)
print(result)

import re
if re.search("[a-z]{5}", "hduef362 327372hwn dh"):
    print('gasit')
else:
    print("Nu s-a gasit")
    
#re.fullmatch
result = re.fullmatch("\w+", string)
print(result)
#If the whole string matches the regular expression pattern, return a corresponding match object.
# Return None if the string does not match the pattern; note that this is different from a zero-length match.

result=re.fullmatch("\w+\s\w+\s\w\s\w+\s\w+\s\w+\s\d+\s\w+", string)
print(result)
#returneaza tot stringul pt ca patternul se potriveste in totalitate cu aceasta

#re.split
print(re.split("\d+", "Maine 10 este 10 sept"))
print(re.split("[aeiou]", "Astazi o sa merg la 1"))

print(re.split(r"\d+", "Maine la ora 12 se fac 2 ani de cand sunt casatoriti"))
print(re.split("\d+", "Maine la ora 12 se fac 2 ani de cand sunt casatoriti"))

#re.sub
#Regexp can also be used to replace an a match with another string using the method sub.
#format is: sub (pattern, replace, string, count=0, flags=0
print(re.sub("\d+", "zero", "In stoc mai sunt 20 rujuri si 5 piepteni"))
print(re.sub("[a-z]", "*", "parola"))

#If replace parameter is a string there is a special operator (\<number>) that if found within the replacement string will be replace with the group from the match search
# (for example \3 will be replaced with .group(3)).
s="Stocul este de 10"
print(re.sub("\w+\s\w+\s\w+\s(\d+)", r"S-au cumparat \1 " , s ))

#utilizarea lui r
print(r"bla"
      r"bla")
#utilizarea inlocuirii unui grup cu o functie
import re
def conver(s):
    return hex(int(s.group(0)))
s="Maine sunt 34 grade "
print(re.sub("\d+", conver, s))

#utilizarea extensiilor
import re
s = "File size if 12345 bytes"
result = re.search("(?P<file_size>\d+)",s)
if result:
    print ("Size is ",result.group("file_size"))

import re
s = "Fisierul este de 12345 bytes"
result = re.search("(?P<nume_document>\w+)",s)
if result:
    print ("Numele documentului este:  ",result.group("nume_document"))

#(?P<name>…) The match object also has a groupdict method that returns a dictionary with all the keys and strings that match the specified regular expression
import re
s = "File config.txt was create on 2016-10-20 and has 12345 bytes"
import re
s = "File config.txt was create on 2016-10-20 and has 12345 bytes"
import re
s = "File config.txt was create on 2016-10-20 and has 12345 bytes"
result = re.search("(?P<name>[A-Za-z\.]+)\s.*(?P<date>\d{4}-\d{2}-\d{2}).*\s(?P<size>\d+)",s)
if result:
    print (result.groupdict())

#building a tokenizer
import re
number = "(?P<number>\d+)"
operation = "(?P<operation>[+\-\*\/])"
braket = "(?P<braket>[\(\)])"
space = "(?P<space>\s)"
other = "(?P<other>.)"
r = re.compile(number+"|"+operation+"|"+braket+"|"+space+"|"+other)
expr = "52 * (250+3-8)."
for matchobj in r.finditer(expr):
    key = matchobj.lastgroup
    print (matchobj.group(key)+" => "+key)


