def iteratorengine(n):
    valor = 0
    for item in range (0,n+1):
        valor = item
        yield item
    for meti in range (n+1,0,-1):
        yield meti+valor

for n in iteratorengine(10):
    print(n)