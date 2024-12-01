#Ejercicio 4
"""Diseñar un algoritmo que lea 20 caracteres de teclado y muestre por pantalla el número de veces que se repiten cada una de las vocales."""



contador_vocal= 0

for i in range(20):
    vocal=(str(input("Introduce el caracter X: ")))
    if vocal == "a" or  vocal == "e" or vocal == "i" or vocal == "o" or vocal =="u":
        contador_vocal = contador_vocal +1
    
        
print(contador_vocal)
