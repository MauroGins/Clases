"""Diseñar un algoritmo que lea del teclado tres números enteros y escriba en pantalla un mensaje indicando si al menos dos de esos tres números son pares."""


"""Resuelto por el profesor"""
print("-------------PROFESOR-----------------")

a = int(input("Introduce un numero : "))
b = int(input("Introduce un numero : "))
c = int(input("Introduce un numero : "))

if (a % 2 == 0 and b % 2 == 0) or (a % 2 == 0 and c % 2 == 0) or (b % 2 == 0 and c % 2 == 0):
        print("Dos de los numeros son pares")
else: 
    print("Al menos dos de los números son impares")