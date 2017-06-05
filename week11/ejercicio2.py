l_usuarios = []
l_clientes = []
l_exclusivos = []

def agregar(lista, persona):
    lista.append(persona)
    print(lista)
    return tuple(lista)
def retirar(lista, persona):
    lista.remove(persona)
    print(lista)
    return tuple(lista)

while True:
    nuevo_dni, nuevo_usuario, tipo_cola = input().split(",")
    personabanco = [nuevo_dni, nuevo_usuario]
    if nuevo_dni=="":
        break
    if tipo_cola == "usuarios":
        if  personabanco not in l_usuarios:
            agregar(l_usuarios, personabanco)
        else:
            retirar(l_usuarios, personabanco)
    elif tipo_cola == "clientes":
        if  personabanco not in l_clientes:
            agregar(l_clientes, personabanco)
        else:
            retirar(l_clientes, personabanco)
    elif tipo_cola == "exclusivos":
        if  personabanco not in l_exclusivos:
            agregar(l_exclusivos, personabanco)
        else:
            retirar(l_exclusivos, personabanco)