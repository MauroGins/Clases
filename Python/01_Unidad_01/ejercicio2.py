#Ejercicio 2
"""Diseñar un algoritmo que calcule y muestre en pantalla el volumen y el área de una esfera para un radio dado"""

import math

radio=int(input("Introduzca el valor del radio: \n"))

area= 4*math.pi*radio**2
vol=(4*math.pi*radio**3)/3


print(f"El área del radio dado es {area}\ny el volumen es {vol}")