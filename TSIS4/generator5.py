def generator(n):
    for i in range (n):
        yield n-i

a = int(input())
g = generator(a)
for x in g:
    print(x)