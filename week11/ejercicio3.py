l_alumnos = {}

def agregar(dict, nombre, vector):
    dict.update({nombre:vector})
def consultar(dict, nombre):
    return dict[nombre]

registro = {}
while True:
    dni = input("DNI:")
    if dni=="":
        break
    nombres = input("Nombre:")
    if nombres=="":
        break
    apellidos = input("Apellidos:")
    if apellidos=="":
        break
    edad = input("Edad:")
    if edad=="":
        break
    carrera = input("Carrera:")
    if carrera=="":
        break

    nombre_completo = apellidos + ", " + nombres
    if nombre_completo not in registro:
        notas = [int(x) for x in input("Notas:").split(",")]
        agregar(registro,nombre_completo,round(sum(notas)/len(notas),2))
        print(registro)
    else:
        print("Las notas del alumno ya se han registrado!")
print(sorted(registro, key=registro.get))