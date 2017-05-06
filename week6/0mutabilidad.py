x = 5
print(id(x))

numeros = [1,2,3,4,5]
print(id(5))
print(id(numeros[4]))

y = [1,2,3,4]
print(id(1))
print(id(2))
print(id(3))
print(id(4))
print(id(y))

x = y
print(id(x))
print(id(x[0]))
print(id(y[0]))

x = [-1,0,1,2]
print(id(x))
print(id(x[3]))
print(id(y[1]))

x[0]=1
print(id(x[0]))
print(id(x[2]))
print(id(y[0]))

z = ("a","b","c","d")
print(z[0])
y = ("z","y","x","a")
print(id(z[0]))
print(id(y[3]))

lista1 = ['a','b','c']
print(lista1)
lista2 = lista1
print(id(lista1),id(lista2))
lista1.append('a')
print(id(lista1),id(lista2))
print(lista1,lista2)

saludo = "Hola UTEC!"
saludo[3]="A"

listan = numeros[:]
print(id(numeros))
print(id(listan))
