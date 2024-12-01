#Ejercicio 6
"""Diseñar un algoritmo que obtenga el promedio de una lista de varlores reales leídos
por teclado. El algoritmo terminará cuándo el usuario introduzca 20 valores."""


num = int(input("Introduce el número de valores reales para calcular  el promedio: "))
suma = 0
contador = 0
while contador < num:
    valor = float(input("Introduce un valor real: "+ str(contador +1)+" /"+" :"))
    suma += valor
    contador += 1
print("El promedio de los valores reales es: ", suma / num)
    
    
num1 = int(input("Introduce valores: "))
suma = 0
contador = 0

while contador < num:
    valor = float(input("Introduce un valor real"+ str(contador +1)+ " /"+": "))
    suma = suma + valor
    contador = contador +1
print("El promedio de los valores reales es: ", suma / num1)
    
    
