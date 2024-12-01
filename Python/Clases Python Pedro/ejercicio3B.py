#DATOS DE ENTRADA
#Pedir al usuario que nos diga la cantidad de segundos a calcular.
segundos_total= int(input("Ingresa los segundos totales: "))

#PROCESAMOS LA INFORMACION
segundos = segundos_total % 60 #Al usar %módulo nos da el resto y el cociendo nos da los minutos.
minutos = segundos_total // 60 #Nos da los minutos
horas = minutos // 60 #Nos da las horas
minutos = minutos % 60 #Nos da los minutos restantes

#DATOS DE SALIDA
print(f"Los segundos que has ingresado {segundos_total} da un total de: {horas} hora/s, {minutos} minuto/s y {segundos} segundp/s")  