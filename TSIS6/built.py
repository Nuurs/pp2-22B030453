def multiple(x):
    arr = []
    for i in range (x):
        a = int(input())
        arr.append(a)
    cnt = 1
    for i in range (x):
        cnt = cnt * arr[i]
    return cnt

x = int(input())
print(multiple(x))
