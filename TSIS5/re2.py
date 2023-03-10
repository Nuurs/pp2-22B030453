import re
x = input()
m = re.search(r"ab{2,3}", x)
print(m)