def factorial(n):
    if n==1:
        return 1
    elif n>1:
        return n*factorial(n-1)
def suma_factorial(n):
    if n==0:
        return 0
    elif n>0 and n%2==0:
        return suma_factorial(n-1)
    elif n>0 and n%2!=0:
        return factorial\
                   (n)+suma_factorial(n-1)
x=int(input())
print(suma_factorial(x))