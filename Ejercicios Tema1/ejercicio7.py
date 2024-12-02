#Diseñar un algoritmo que calcule y muestre en pantalla el factorial de un número entero dado.

    
import math

print("Introduce el numero del cual quieres conocer el factorial")
n = int(input())

result = math.factorial(n)

print(f"El factorial de {n} es {result}")


"""Resuelto por el profesor"""
print("-------------PROFESOR-----------------")


print("Calcular el factorial")

n= int(input())

factorial = 1

for i in range (1,n+1):
    factorial *= i
print(f"El facorial de {n} es {factorial}")
    
    
"""Resuelto por el profesor"""
print("-------------PROFESOR OPCION 2 CON WHILE-----------------")

n= int(input("introduce factorial"))

factorial = n
i = n
while i > 1:
    i -= 1
    factorial *= i
print(f"El favtorial de {n} es {factorial}")