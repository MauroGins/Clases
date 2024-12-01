"""
Convertir tiempo a segundos
""" 

#DATOS DE ENTRADA
#Pedir al usuario que nos diga la cantidad de segundos a calcular.
segundos_total= int(input("Ingresa los segundos totales: "))



#PROCESAMOS LA INFORMACION
#Dividimos el valor total de segundos entre 3600(segundos en 1h0)
horas= segundos_total // 3600 #División entera para evitar decimales
#El resto de la división atnerior será lo que tengo que seguir dividiendo para poder 
#calcular los minutos y segundos.
segundos_restantes = segundos_total % 3600 #Obtenemos el resto de la división (que es lo que neceistamos)
#Dividimos el resto entre 60  para obtener los minutos.
minutos = segundos_restantes // 60 #División entera para evitar decimales
#El resto de la división anterior entre 60  nos da los segundos.
segundos = segundos_restantes % 60 #Obtenemos el resto de la división

#DATOS DE SALIDA
print(f"Los segundos que has ingresado {segundos_total} da un total de:  {horas} hora/s, {minutos} minuto/s y {segundos} segund/s")  #



