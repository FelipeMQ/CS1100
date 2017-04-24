# programa para que imprima un mensaje
# dependiendo de la universidad y carrera
# del usuario

universidad = input('ingrese universidad: ')
carrera = input('ingrese carrera: ')

if universidad == 'UTEC':
    print('Bienvenido a UTEC')

    if carrera == 'industrial':

        print('Tu carrera es industrial')

    else:

        print('Tu carrera no es industrial')


