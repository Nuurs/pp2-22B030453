def generator_(n):
    for i in range(n):
        if(i%3==0 and i%4==0):
            yield i

a = int(input())
g = (generator_(a))
for x in g:
    print(x)
    