"""
EJERCICIO 2: Escribe un programa en Python que dadas las coordenadas por teclado x e y de dos puntos en el plano, 
muestre por pantalla la distancia que existe entre esos dos puntos:
"""
import math

#DATOS DE ENTRADA
#pedimos las coordenadas de los dos puntos
x1 = float(input("Introduce coordenada x1: ")) 
y1 = float(input("Introduce coordenada y1: ")) 

x2 = float(input("Introduce coordenada x2: ")) 
y2 = float(input("Introduce coordenada y2: ")) 

#PROCESAR INFORMACION
#calcular la distancia sin utilizar libreria de Python
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(round(distancia, 2))

#calcular la distancia utilizando la libreria math de Python
distancia = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
print(round(distancia, 2))