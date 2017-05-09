import math

n = int(input())

suma=0
for i in range(1,n+1,2):
    suma=suma+math.factorial(i)
print(suma)