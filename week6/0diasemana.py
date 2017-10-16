segundos = int(input())

dia_semana = ['domingo','lunes','martes','miercoles','jueves','viernes','sabado']

segundos_por_dia = 86400
posicion_dia = (segundos//segundos_por_dia) % 7
print(dia_semana[posicion_dia])