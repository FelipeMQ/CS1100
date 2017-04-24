import math

def suma1(num1):
    return num1*(num1+1)/2

def suma2(num2):
    if num2==1:
        return 1
    else:
        return num2+suma2(num2-1)

def suma3(num3):
    return math.fsum(range(1,num3+1))

valor = int(input())
print(suma3(valor))
