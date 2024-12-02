"""Diseñar un algoritmo que calcule la suma de todos los números comprendidos entre 1 y 500 que cumplan la condición de ser múltiplos de 5 y de 7.
Para verificar si un número X es múltiplo de otro número Y, basta con comprobar si el resto de la división entera de X entre Y es igual a 0."""

calculo = 0

for i in range(1, 501):
    if i % 5 == 0 and i % 7 == 0:
        calculo += i
print(calculo)