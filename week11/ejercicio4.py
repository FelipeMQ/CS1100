l_personas = {}

def agregar(dict, nombre, vector):
    dict.update({nombre:vector})
def consultar(dict, nombre):
    return dict[nombre]

registro = {}
while True:
    nombre = input("Ingrese nombre:")
    if nombre=="":
        break
    else:
        if nombre not in registro:
            vector = input("Ingrese vector:").split(",")
            agregar(registro,nombre,vector)
            print(registro)
        else:
            print(consultar(registro,nombre))