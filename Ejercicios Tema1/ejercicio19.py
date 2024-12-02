#Ejercicio 19

#Diseñar un algoritmo que lea un conjunto de números reales, los cuente y calcule
# y muestre la media, varianza y la desviación típica del conjunto de números. La
# media y la varianza se calculan con las fórmulas:
#
#   Media = (suma de los números) / (número de números).
#   Varianza = ((suma de los cuadrados de los números) - (suma de los números)^2 / (número de números)).
#   La desviación típica es la raíz cuadrada de la varianza.
import math

sumatorio = 0 
sumatorio_cuadrados = 0


n_vueltas = int(input("introduzca el numero de veces que va a introducir de numeros: "))

if n_vueltas <=0:
    print("el numero de vueltas debe ser mayor que 0")
else:
    for i in range(n_vueltas):
        num = float(input("Introduzca un número: "))
        sumatorio += num
        sumatorio_cuadrados += num **2
    else: 
        media = sumatorio /n_vueltas
        varianza = (sumatorio_cuadrados - (sumatorio ** 2) / n_vueltas) / n_vueltas
        desviacion_tipica = math.sqrt(varianza) # desviacion_tipica = varianza ** 0.5 para no usar math
        print(f"Media: {media}")
        print(f"Varianza: {varianza}")
        print(f"Desviación típica: {desviacion_tipica}")  #
        