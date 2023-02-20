def generator(a,b):
    arr = []
    for i in range(a,b):
        arr.append(i**2)
    return arr
a = int(input())
b = int(input())
print(generator(a,b))
