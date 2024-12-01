
#ENTRADA DE DATOS
#pedir al usuario la cantidad de segundos
segundos_total = int(input("Introduce segundos totales: "))

#PROCESO DE LA INFORMACION
segundos = segundos_total % 60 #=> segundos

#dividimos los segundos totales entre 60 para que nos quede para
#calcular los minutos y las horas
minutos = segundos_total // 60

#divimos el resultado que se nos ha quedado anterior entre 60 => minutos
minutos = minutos // 60

#el resto de la division anterior serán las horas
horas = minutos % 60

#SALIDA DE DATOS
print(segundos_total, "segundos =", horas, "hora/s", minutos, "minuto/s", segundos, "segundos")