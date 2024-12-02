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

total = (int(input("Introduce la totalidad de la cuenta: \n")))
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

if palabra == reversed(palabra):
    print(palindromo)
else:
    print("No es un palindormo")









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


# Datos del día actual
anyo_actual=2024
dia_actual=16
mes_acutal=10
One_year = 365

print(f"Hoy es {dia_actual}/{mes_acutal}/{anyo_actual}: \n")
anyo= -1
anyo = int(input("Introduce el año que has nacido: \n"))
if anyo == anyo_actual:
    print(f"Hoy es el mes{anyo_actual}")
elif anyo <0:
    print("El año introducido no es válido. \n")

mes = -1
mes = int(input("Introduce el mes en el que has nacido: \n"))
if mes == mes_acutal:
    print()
elif mes >= 13 or mes <=0:
    print("El mes introducido no es válido. \n")
    
    
dia = -1
dia = int(input("Introduce el día que has nacido: \n"))
if dia == dia_actual:
    if mes == mes_acutal:
        print("Hoy es tu cumpleaños!!!")
else:
    print("Te falta poco para tu cumpleaños!!") 

edad= anyo_actual-anyo


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


tamano = int(input("Introduce un número entero para la altura del rombo (valor mínimo <<3>>): \n"))
espacio = " "
if tamano <=2: 
    print("El tamaño de la altura ha de ser mayor de 3")
else: 
    for i in range(tamano-1):
       
        print(" *" + " " * (tamano)+ "*")
            
    else:
        print("   " + "*" * (tamano-1))









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

numero = int(input("Introduce un número: \n").isdigit())
cuenta = 0


print(numero)



    




print("-"*20)

print("Ejercicio 5 - Jugando con los dígitos - versión for")








print("-"*20)