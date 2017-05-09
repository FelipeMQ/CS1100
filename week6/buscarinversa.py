vocales = ['a','e','i','o','u','z','q']

for i in range(-1,-1-len(vocales),-1):
    print(vocales[i], end=" ")

print()
for i in range(len(vocales)-1,-1,-1):
    print(vocales[i], end=" ")
