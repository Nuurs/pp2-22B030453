import re
x = input()
m = re.findall(r"[a-z]+\_", x)
print(m)