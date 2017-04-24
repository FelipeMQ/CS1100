import math, time


def fiba(n):
    if n < 2: return 1
    return fiba(n - 1) + fiba(n - 2)


def fibb(n):
    if n < 2: return 1
    return fibb((n + 1) / 2) * fibb(n / 2) + fibb((n - 1) / 2) * fibb((n - 2) / 2)


def fibc(n):
    if n < 2: return 1
    return int((1 / math.sqrt(5)) * math.pow((1 + math.sqrt(5)) / 2, n + 1) - (1 / math.sqrt(5)) * math.pow((1 - math.sqrt(5)) / 2,n + 1))


def timestamp():
    return int(round(time.time() * 1000))


def fibo(n, clase):
    t1 = timestamp()
    if (clase == "a"):
        termino = fiba(n)
    if (clase == "b"):
        termino = fibb(n)
    if (clase == "c"):
        termino = fibc(n)
    print("Tiempo termino[",n,"]: ", timestamp()-t1)
    #print(termino, ";", timestamp() - t1)

fibo(35, "a") #5000ms
fibo(5000, "b") #5000ms
fibo(1473, "c") #0ms
