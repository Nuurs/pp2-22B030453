import re

t = input("")

arr = re.findall("[A-Z]", t)
arr2 = ["_" + c.lower() for c in arr]


for i in range(len(arr)):
    x = t.find(arr[i])
    t = t[0: x] + arr2[i] + t[x + 1: ]

print(t)
