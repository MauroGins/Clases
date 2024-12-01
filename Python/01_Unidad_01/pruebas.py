print("Ejercicio 5 - Jugando con los dígitos - versión while")

numero = int(input("Introduce un número entero positivo: "))

if numero < 0: 
    print("Número no válido")
else:
    suma = 0
    contador = 0
    while numero > 0:
        suma += numero % 10
        numero = numero // 10
        contador += 1

    print("El resultado de la división es:", suma/contador)