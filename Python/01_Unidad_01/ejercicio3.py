#Ejercicio 3
"""Diseñar un algoritmo que pida una nota (valor entero)
por teclado y dependiendo de su valor visualice la nota en letras.
Por ejemplo, si nota es igual a 7 tiene que mostrar el texto "Notable"."""

nota =-1

while nota <0 or nota >10:


    nota = int(input("Introduce la nota de [0-10]: \n"))

    match nota:
        case 0|1|2|3|4:
            print("Suspenso")
        case 5:
            print("Suficiente")
        case 6:
            print("Bien")
        case 7|8:
            print("Notable")
        case 9|10:
            print("Sobresaliente")
        case _:
            print("El valor de la nota es invalido.")