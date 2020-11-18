s1="pisica, caine"
s2="pisica, caine, cal, vaca, pisica, caine"
import re
result=len(re.findall(s1, s2))
print(result)