import re
x = input()
m = re.findall(r"a.+b\Z", x)
print(m)