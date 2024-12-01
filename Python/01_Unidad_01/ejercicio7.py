"""Diseñar un algoritmo que calcule y muestre en pantalla el factorial de un número entero dado."""

n=int(input("Introduce un numero del cual quieras saber su factorial "))
contador = 1
factorial = 1


while contador <= n:
    factorial =  factorial * contador
    contador += 1


print(factorial)
