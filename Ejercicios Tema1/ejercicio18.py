# Ejercicio 18
# Diseñar un algoritmo que lea una lista de 10 números enteros,
# visualice la suma de los pares, cuántos pares existen y cuál es
# la media aritmética de los números impares.

suma_pares = 0
suma_impares = 0
n_pares = 0

for i in range(10):
    num = int(input("Introduzca un número: "))
    if num % 2 == 0:
        suma_pares += num
        n_pares += 1
    else:
        suma_impares += num
        
print("La suma de los pares es:", suma_pares)
print("El número de pares es:", n_pares)
print("La media de los impares es: ", suma_impares /(10 -n_pares))


#versión anvanzada del ejercicio pidiendo el numero de veces que van a introducir los numeros

suma_pares = 0
suma_impares = 0
n_pares = 0

n_vueltas = int(input("introduzca el numero de veces que va a introducir de numeros: "))

if n_vueltas <=0:
    print("el numero de vueltas debe ser mayor que 0")
else:
    for i in range(n_vueltas):
        num = int(input("Intoduzca un número: "))
        if num % 2 == 0:
            suma_pares += num
            n_pares  += 1
        else: 
            suma_impares  += num


    print("La suma de los pares es:", suma_pares)
    print("El número de pares es:", n_pares)
    print("La media de los impares es: ", suma_impares /(10 -n_pares))

            