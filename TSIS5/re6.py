import re
x = input()
print(re.sub(r"[ ,.]", ":", x))