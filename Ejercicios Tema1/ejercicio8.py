"""Realizar un algoritmo que calcule y muestre en la pantalla la suma de los n primeros enteros impares. El valor de n se solicitará al usuario."""

n = int(input("Ingrese el valor de n: "))
suma = 0
while i <= n * 2:
    if i % 2 != 0:
        suma += i
    i += 1
print(f"La suma de los {n} primeros enteros impares es: {suma}")


"""Resuelto por el profesor"""
print("-------------PROFESOR-----------------")
for i in range(1, n * 2, 2):
    suma += 1
print(f"La suma de los {n} primeros impares es {suma}")


"""Resuelto por el profesor"""
print("-------------PROFESOR-----------------")


suma = 0
for i in range(1, n + 1):
    suma += 2 * i - 1
print(f"La suma de los {n} primeros impares es {suma}")


"""Resuelto por el profesor"""
print("-------------PROFESOR CON WHILE-----------------")


suma = 0
i = 1

while i <= n:
    suma += 2 * i - 1
    i += 1
print(f"La suma de los {n} primeros impares es {suma}")


"""Resuelto por el profesor"""
print("-------------PROFESOR CON WHILE-----------------")


suma = 0
i = 1

while i <= n:
    suma += 2 * i - 1
    i += 1
print(f"La suma de los {n} primeros impares es {suma}")
