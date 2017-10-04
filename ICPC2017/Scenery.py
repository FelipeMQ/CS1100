import sys


def calcularacople(n, t, lista, linter):
    if len(linter) > 0:
        delta, der, izq, suma = 0, 0, 0, 0
        for i in range(n):
            if lista[i][0] < linter[0]:
                izq = linter[0] - lista[i][0]
            if lista[i][1] > linter[-1]:
                der = lista[i][1] - linter[-1]
            if izq > der:
                delta = izq
            else:
                delta = der
            suma += (t - delta)
        if len(inter) > suma:
            return "yes"
        else:
            return "no"
    else:
        return "yes"

n,t = [int(x) for x in input().split(" ")]

if n < 10000 and t < 100000:
    lista = []
    for i in range(n):
        lista.append([])

    for i in range(n):
        lista[i] = [int(x) for x in input().split(" ")]
        if lista[i][0] < 0:
            lista[i][0] = 0
        if lista[i][1] < 0:
            lista[i][1] = 0
        if lista[i][1] < lista[i][0]:
            lista[i][0], lista[i][1] = lista[i][1], lista[i][0]
        if lista[i][0] + t > lista[i][1]:
            print("no")
            sys.exit()

    intset = set()
    for i in range(n):
        intset = intset | set(range(lista[i][0], lista[i][1] + 1))

    inter = intset
    for i in range(n):
        inter = inter & set(range(lista[i][0], lista[i][1] + 1))

    print(calcularacople(n, t, lista, list(inter)))

else:
    sys.exit()
