# Estructura secuencial

#Definidas variables

a = 5
b = int(input("Numero a ingresar"))
suma = a + b

#1. Ingresar dos números y mostrar la suma

print("La suma de", a, "y", b, "es", suma)

#2. Concatenación (Hay que pones str delante de los strings para que no confunda el sumar con la concatenación.)

print("La suma de " + str(a) + " y " + str(b) + " es " + str(suma))

# Estructuras condicionales (van a partir de un if)

if suma >10: 
    print("La suma es mayor que 10")
if suma == 13:
    print("La suma es 13")
print("Fin del programa")


# Alternativa if else (si sino)

if suma >10: 
    print("La suma es mayor que 10")
else: 
    print("La suma es menor o igual que 10")


if suma == 13:
    print("La suma es 13")
print("Fin del programa")

# Estructura condicional Selectiva  [Ejercicio3]


#Bucles 
#Bucle for para variables:

#ejemplo1

for i in range(5):
    print(i)

#ejemplo2
for i in range(1,6):
    print(i)

#ejemplo 3 el valor primero es el numero donde empieza, el segundo es hasta donde de maximo y no se muestra y el tercero es cual es la consecución.

for i in range(1,10,2):
    print(i)

#ejemplo 4

for i in range(10,0,-1):
    print(i)

#ejemplo 5
#En cada vuelta del bucle coge la primera letra hasta la ultima

palabra = "Python"
print(len(palabra))
for letra in palabra:
    print(letra, end="-")


