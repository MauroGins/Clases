# Resuelve los siguientes ejercicios sin modificar ninguna de las lineas de código existentes.
# Nota: no se pueden modificar las líneas pero si se pueden añadir líneas de código entre las de inicio y final si se necesita más espacio.

# Ejericio 1 (2 puntos)

"""
Diseña un algoritmo que calcule la cantidad de propinas que se deben dar en un restaurante.
El algoritmo debe leer de teclado el total de la cuenta y preguntarle al usuario si su servicio fue bueno, malo o regular.
Para saber la opción elegida por el usuario, se debe indicar que el usuario debe escribir "bueno", "malo" o "regular",
 puede escribirlo en minúsculas, mayúsculas o combinando ambas y debe funcionar igual.   
En caso de que el servicio haya sido bueno, el algoritmo debe calcular el 20% del total de la cuenta.   
En caso de que el servicio haya sido regular, el algoritmo debe calcular el 15% del total de la cuenta.
En caso de que el servicio haya sido malo, el algoritmo debe calcular el 10% del total de la cuenta.
Finalmente, el algoritmo debe imprimir el total de la cuenta más la propina y el total de la propina, por separado.   
"""

print("Ejercicio 1 - Calculadora de propinas")

total = (float(input("Introduce la totalidad de la cuenta: \n")))
propina = (input("Como calificaría su servicio? malo, regular, bueno: \n")).lower() 

match propina:
    case "malo":
        propina = total * 0.1
    case "regular":
        propina = total * 0.15
    case "bueno":
        propina = total * 0.20
    case _:
        print("No has seleccionado ninguna opción válida")


total_cuenta = total + propina 

print("El total de la cuenta es:", total_cuenta, "€ y la propina es: ", propina, "€.")

print("-"*20)

# Ejericio 2 (2 puntos)


"""
Diseñar un algoritmo que nos diga si la palabra introducida por el usuario es un palíndromo o no.   
Un palíndromo es una palabra que se lee igual de izquierda a derecha que de derecha a izquierda.    
Por ejemplo, la palabra "oso" es un palíndromo.
El algoritmo debe leer una palabra del usuario y comprobar si es un palíndromo o no.
"""
print("Ejercicio 2 - Comprobador de palíndromos")

palabra = input("Introduce una palabra: ")
palindromo = "Es un palindromo"
no_palindromo = "No es un palindromo"
palabra = palabra.lower()
palabra_invertida = palabra[::-1]

match palabra, palabra_invertida:
    case palabra, palabra_invertida if palabra == palabra_invertida:
        print(palindromo)
    case palabra, palabra_invertida if palabra != palabra_invertida:
        print(no_palindromo)
        
        
print("-"*20)


# Ejericio 3 (2 puntos)

"""
Diseñar un algoritmo que calcule la edad de una persona en función de su fecha de nacimiento.
El algoritmo debe leer el año, mes y día de nacimiento de la persona y calcular su edad a día de hoy.
Hay que comprobar que la fecha de nacimiento es válida, aunque se da por hecho que los datos introducidos
por el usuario serán números enteros.
Finalmente, el algoritmo debe imprimir la edad de la persona.
"""
print("Ejercicio 3 - Calculadora de edad")#Datos de examen

# Leer fecha de nacimiento
anio_nacimiento = int(input("Introduce el año de nacimiento: "))
mes_nacimiento = int(input("Introduce el mes de nacimiento (1-12): "))
dia_nacimiento = int(input("Introduce el día de nacimiento (1-31): "))

# Obtener la fecha actual
anio_actual = 2024  # Cambia esto a la fecha actual
mes_actual = 10     # Cambia esto a la fecha actual
dia_actual = 16     # Cambia esto a la fecha actual

# Comprobar que la fecha de nacimiento es válida
if (mes_nacimiento < 1 or mes_nacimiento > 12) or (dia_nacimiento < 1 or dia_nacimiento > 31):
    print("La fecha de nacimiento es inválida")
    exit()

# Comprobar si el día es válido para el mes
if (mes_nacimiento == 2 and dia_nacimiento > 29) or \
   (mes_nacimiento in [4, 6, 9, 11] and dia_nacimiento > 30):
    print("La fecha de nacimiento es inválida")
    exit()

# Calcular edad
edad = anio_actual - anio_nacimiento

# Ajustar si el cumpleaños aún no ha ocurrido este año
if (mes_actual < mes_nacimiento) or (mes_actual == mes_nacimiento and dia_actual < dia_nacimiento):
    edad -= 1

# Imprimir edad
print("La edad de la persona es:", edad, "años")#Datos de examen

print("-"*20)#Datos de examen

# Ejericio 4 (2 puntos)

"""
Diseña un algoritmo que pinte por pantalla un rombo hueco con asteriscos.
El programa debe pedir la altura del rombo al usuario y pintar el rombo con esa altura.
Se debe comprobar que la altura mínima es igual o mayor a 3, y además, que la altura es un número impar.    
En caso de que no se cumplan los requisitos, el programa debe imprimir un mensaje de error y volver a pedir el dato al usuario. 
"""

# Ejemplo de salida para una altura de 5:
#   *
#  * *
# *   *
#  * *
#   *

print("Ejercicio 4 - Rombo hueco")# Datos de examen


# Pedir altura al usuario
while True:
    altura = int(input("Introduce la altura del rombo (debe ser un número impar y mayor o igual a 3): "))
    if altura >= 3 and altura % 2 == 1:
        break
    else:
        print("Error: La altura debe ser un número impar y mayor o igual a 3.")

# Dibujar el rombo
for i in range(altura // 2 + 1):
    # Espacios en blanco
    for j in range(altura // 2 - i):
        print(" ", end="")
    # Asteriscos
    print("*", end="")
    if i > 0:  # Para no imprimir el espacio entre asteriscos en la primera línea
        for j in range(2 * i - 1):
            print(" ", end="")
        print("*", end="")
    print()  # Nueva línea

for i in range(altura // 2 - 1, -1, -1):
    # Espacios en blanco
    for j in range(altura // 2 - i):
        print(" ", end="")
    # Asteriscos
    print("*", end="")
    if i > 0:  # Para no imprimir el espacio entre asteriscos en la última línea
        for j in range(2 * i - 1):
            print(" ", end="")
        print("*", end="")
    print()  # Nueva línea


print("-"*20)

# Ejericio 5 (2 puntos - 1 punto cada versión - Jugando con los dígitos) 

"""
Diseñar un algoritmo que pida al usuario un número entero y calcule la suma de los dígitos de ese número.
Una vez tenga la suma calculada debe dividir el resultado entre el total de dígitos que tiene el número.
Finalmente, el algoritmo debe imprimir el resultado de la división.
Hay que controlar el que el número introducido por el usuario sea positivo.
Este ejercicio hay que resolverlo de dos maneras, es decir, debes hacer dos versiones del algoritmo:
Una con un bucle while y con un bucle for. Cada versión debe tener su propio código y no se pueden mezclar.
Cada versión del algoritmo tendrá un valor de 1 punto.
"""

print("Ejercicio 5 - Jugando con los dígitos - versión while")
# Pedir número al usuario
while True:
    num = int(input("Introduce un número entero positivo: "))
    if num > 0:
        break
    else:
        print("Error: El número debe ser positivo.")

# Calcular suma de dígitos
suma = 0
digitos = 0
n = num
while n > 0:
    digito = n % 10
    suma += digito
    digitos += 1
    n //= 10

# Calcular promedio
promedio = suma / digitos

# Imprimir resultado
print("El resultado de la división es:", promedio)

print("-"*20)

print("Ejercicio 5 - Jugando con los dígitos - versión for")

# Pedir número al usuario
while True:
    num = int(input("Introduce un número entero positivo: "))
    if num > 0:
        break
    else:
        print("Error: El número debe ser positivo.")

# Calcular suma de dígitos
suma = 0
digitos = 0
for digito in str(num):
    suma += int(digito)
    digitos += 1

# Calcular promedio
promedio = suma / digitos

# Imprimir resultado
print("El resultado de la división es:", promedio) 

print("-"*20)