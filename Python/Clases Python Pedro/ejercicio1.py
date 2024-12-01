#Ejercicio 1.

#DATOS DE ENTRADA
#Pedir la nota de teoria y practicas

notaT= float(input("Introduce la nota de teoria: "))
notaP= float(input("Introduce la nota de prácticas: "))

#PROCESAR LA INFORMACION
#Calcular la nota final
notaFinal=notaT*0.7 + notaP*0.3

#DATOS DE SALIDA
#Resultado final
print(f"La nota final es {round(notaFinal,2)}")