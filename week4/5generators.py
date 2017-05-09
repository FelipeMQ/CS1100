x,y = [1,2,3,1,2,3,3],[4,3,3,4,3,4,3]
plain = zip(x,y)

suma = [a*b for a,b in zip(x,y)]

print(suma)

for x,y in plain:
    print(x,y)


def iteratorengine(n):
    valor = 0
    for item in range (0,n+1):
        valor = item
        yield item
    for meti in range (n+1,0,-1):
        yield meti+valor


for n in iteratorengine(10):
    print(n)