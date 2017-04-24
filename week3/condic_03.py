# Muestre la bonificación que le corresponde a un trabajador,
# dependiendo de los años de servicio.

bonificacion = 0
anio_servicio = int(input('Ingrese años de servicio: '))


#if 2 <= anio_servicio <= 4:
if anio_servicio >= 2 and anio_servicio <= 4:
    bonificacion = 500
elif 5 <= anio_servicio <= 10:
    bonificacion = 700

print(bonificacion)

# complete las condiciones segun el enunciado
