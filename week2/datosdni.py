datos = input()
pos_dni = datos.index(' ')
dni = datos[0:pos_dni]

nombre_completo = datos[pos_dni+1:len(datos)]
pos_nombre = nombre_completo.index(' ')
nombre = nombre_completo[0:pos_nombre]

apellidos = nombre_completo[pos_nombre+1:len(nombre_completo)]
pos_apepat = apellidos.index(' ')
apellido_paterno = apellidos[0:pos_apepat]

apellido_materno = apellidos[pos_apepat+1:len(apellidos)]

print("DNI:",dni)
print("NOMBRE:",nombre)
print("APELLIDO PATERNO:",apellido_paterno)
print("APELLIDO MATERNO:",apellido_materno)