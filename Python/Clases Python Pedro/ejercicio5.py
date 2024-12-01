"""
Diseñe un programa que resuelva una ecuación de segundo grado ax^2+bx+c=0 . Debe
pedir al usuario que introduczca los valores de a,b,c de tipo entero y el programa 
indicará si tiene dos raíces solución,o bien si sólo tiene una raíz solución
o bien un mensaje expresando que no tiene raícesreales. Indicar en cada caso el 
valor de las soluciones posibles.
"""
#ENTRADA DE DATOS
#Pedir los 3 coeficientes de la ecuación
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))

#PROCESO
#Calcular el discriminante

discriminante = b**2 - 4*a*c

#Determinar el tipo de raíces que tiene la ecuación 
if discriminante == 0:
    print("Tiene una única raíz real.")
    #Calculamos la única solución
    raiz = -b / (2 * a)
    print("La raíz real es: ", raiz)
elif discriminante  > 0:
    #Calculamos las dos soluciones
    print("La ecuación tiene dos soluciones reales.")
    #Solucion 1
    raiz1 = (-b + discriminante ** 0.5) / (2 *a)
    #Solucion 2
    raiz2 = (-b - discriminante ** 0.5) / (2 *a)
    print(f"Las raíces reales son: {raiz1} y {raiz2}")
else:
    print("La ecuación no tiene solución real.")



