
#ENTRADA DE DATOS
#pedir al usuario la cantidad de segundos
segundos_total = int(input("Introduce segundos totales: "))

#PROCESO DE LA INFORMACION
#divido el valor de segundos total entre 3600 => horas
horas = segundos_total // 3600

#el resto de la división anterior será lo que tengo que seguir
#dividiendo para poder calcular los minutos y segundos
resto = segundos_total % 3600

#divido el resto entre 60 => minutos
minutos = resto // 60

#el resto de la división anterior entre 60 => segundos
segundos = resto % 60

#SALIDA DE DATOS
print(segundos_total, "segundos =", horas, "hora/s", minutos, "minuto/s", segundos, "segundos")