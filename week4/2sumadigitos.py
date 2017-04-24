def sumadigitos(num):
    suma = 0
    for digito in num:
        suma = suma + int(digito)
    return suma

def sumadigitos2(num):
    if num<10:
        return num
    else:
        return (num % 10) + sumadigitos2(num // 10)

n = int(input())
print(sumadigitos2(n))
