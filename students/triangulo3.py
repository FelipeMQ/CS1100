a = int(input())
b = "A BCDEFGHIJKLMNÑOPQRSTUVWXYZ"
c = a
d = 1
e= 1
def f(e):
    if e == 1:
        return "A"
    else:
        return f(e-1)+" "+b[e]
if 0<a<28:
    while d <= a:
        print (" "*(c-1)+f(e))
        c -=1
        d +=1
        e +=1
else:
    print("Valor incorrecto")