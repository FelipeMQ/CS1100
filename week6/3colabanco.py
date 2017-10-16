cola = []
persona = []

i=0
while True:
    dni_anterior = None
    ingreso = input()
    if ingreso == 'FIN':
        break
    else:
        dni, edad, nombre = ingreso.split(' ')
        if i>0:
            persona[i-1][3] = dni
        persona.append([dni, edad, nombre, None])
        print(persona)
        cola.append([dni])
        print(cola)
    i=i+1
