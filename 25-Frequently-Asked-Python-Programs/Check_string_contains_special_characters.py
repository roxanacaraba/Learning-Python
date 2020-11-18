import  re
s="Te&iubesc$tef@n"
regex=re.compile('[@_!#$%^&*()<>?/\|}{~:]')
if (regex.search(s)==None):
    print("No special characters present in string")
else:
    print("String contains special characters")
