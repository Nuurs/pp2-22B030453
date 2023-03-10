import re
x = input()
m = re.findall(r"[A-Z]", x)

print(m)