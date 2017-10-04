letra = input()
if (letra in ['a','e','i','o','u']):
    print("es una vocal abierta")
elif (letra in ['i','u']):
    print("es una vocal cerrada")
else:
    print("es una consonante")