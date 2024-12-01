"""
EJERCICIO 1: Escribe un programa en Python pida la nota de teoría y la nota de prácticas al usuario 
y calcule la nota final teniendo en cuenta que ésta será un 70% la nota de teoría y un 30% 
la nota de prácticas.
"""

#DATOS DE ENTRADA
#pedir la nota de teoria y de practicas
notaT = float(input("Introduce la nota de teoria: "))
notaP = float(input("Introduce la nota de prácticas: "))

#PROCESAR INFORMACION
#calcular la nota final
notaFinal = notaT * 0.7 + notaP * 0.3

#DATOS DE SALIDA
print("La nota final es:", round(notaFinal, 2))
print(f"La nota final es: {round(notaFinal, 2)}")