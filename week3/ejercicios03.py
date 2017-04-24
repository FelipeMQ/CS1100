# escriba un programa que permita hallar las raices de una ecuacion
# cuadratica. si se conoce la formula cuadratica

import math

A = float(input('Ingrese A: '))
B = float(input('Ingrese B: '))
C = float(input('Ingrese C: '))

discriminante = B**2 - 4*A*C
if discriminante > 0:
    raiz1 = (B + math.sqrt(discriminante))/2*A
    raiz2 = (-1*B - math.sqrt(discriminante))/2*A

    print('las raices son: ', raiz1, " y ", raiz2 )
else:
    print('Raices imaginarias')
