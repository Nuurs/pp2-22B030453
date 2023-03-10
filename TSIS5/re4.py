import re
x =input()
m = re.findall("[A-Z][a-z]+", x)
print(m)