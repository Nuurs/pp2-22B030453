import re
x = input()
m = re.search(r"ab*", x)
print(m)