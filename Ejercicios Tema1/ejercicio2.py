# Diseñar un algoritmo que calcule y muestre en pantalla el volumen y el área de una esfera para un radio dado.
# Volumen(4/3)*pi*r^3
# Area 4*pi*r^2

# Pi es FLOAT

import math


r = float(input("Introduce el radio "))

v = (4 / 3) * math.pi * r**3
print("El volumen es", v)

a = 4 * math.pi * r**2
print("El área es", a)
