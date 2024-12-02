#Ejercicio 20
# Diseñar un algoritmo que lea un número entero de teclado,
# visualice sus dígitos y calcule la suma de los dígitos que 
# sean pares. Para extraer los dígitos de un número usaremos 
# un bucle que divida el número por 10 sucesivamente. El resto
# de cada división corresponde a cada uno de los dígitos.


sum_pares = 0
numero = int(input("Ingrese un número entero: "))

while numero != 0:
    digito = numero % 10
    print("Digito", digito)
    if digito % 2 == 0:
        sum_pares += digito
    numero //= 10
print("La suma de los dígitos pares es:", sum_pares)


