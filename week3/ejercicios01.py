# Escribir un programa que permita leer como dato el PH y el programa
# indique el tipo de solucion
# El tipo de solusion se determina segun la siguiente tabla:

"""
    |-----------------------------------|
    |    PH        Solution Category    |
    |-----------------------------------|
    |   0-4         Strong acid         |
    |   5-6         Weak acid           |
    |   7           Neutral             |
    |   8-9         Weak base           |
    |   10-14       Strong base         |
    |-----------------------------------|

"""

valor_PH = int(input('Ingrese el valor del PH: '))

if valor_PH >=0 and valor_PH <= 4:
    solucion = 'Strong acid'
elif valor_PH >= 5 and valor_PH <= 6:
    solucion = 'Weak acid'
# Complete el resto de condiciones

print(solucion)
