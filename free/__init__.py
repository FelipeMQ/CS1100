def comb(n, m):
    if n < 1 or m < 1 or n > 1000 or m > 1000:
        print("Valor incorrecto")
    else:
        print(fact(n) // (fact(m) * fact(n - m)))


def fact(k):
    if k == 1:
        return 1
    else:
        return k * fact(k - 1)


n, m = input().split(",")
n = int(n)
m = int(m)
comb(n,m)