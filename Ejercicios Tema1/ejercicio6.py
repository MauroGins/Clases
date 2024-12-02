#Diseñar un algoritmo que obtenga el promedio de una lista de varlores
#reales leídos por teclado.
#El algoritmo terminará cuándo el usuario introduzca 20 valores.

######################
"""Primera opción"""
######################

print("Ingrese 20 valores")

suma = 0
contador = 0

while contador < 20:
    print("ingresar un valor" +  str(contador +1 ) + "/20")
    valor = float(input())
    suma += valor
    contador +=1
    
    
promedio = suma / 20
print("El promedio es: " + str(promedio))



######################
"""Segunda opción// Pide el promedio  y el número de valores para ese promedio"""

######################

n = int(input("Ingrese el número de valores reales, para calcular su promedio: "))
suma = 0
contador = 0

while contador < n:
    print("ingresar un valor" +  str(contador +1) + "/" + str(n) + ": ")
    valor = float(input())
    suma += valor
    contador +=1
    
    
promedio = suma / n
print("El promedio es: " + str(promedio))