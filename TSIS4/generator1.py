def generator_(n):
    arr = []
    for i in range (n):
        arr.append(i**2)
    return arr

a = int(input())
print(generator_(a))