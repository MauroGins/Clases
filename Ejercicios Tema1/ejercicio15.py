# Ejercicio 15
"""
Diseñar un algoritmo que lea una secuencia de 20
números reales introducidos por teclado. Al acabar
la secuencia, debe mostrar el valor máximo y mínimo 
introdcidos.
"""

max = float(input("Introduce un número inicial: "))# Pedimos el primer número
min = max  # Inicializamos min con el primer número

for i in range(19): # Bucle para leer los 19 números restantes
    num = float(input("Introduzca un número: ")) # Pedimos un numero
    if num > max: #Si es mayor que max
        max = num #actualizas el máximo
    if num < min: #Si es menor que min
        min = num #actualizas el mínimo
        
print("El minimo es", min,"El maximo es",max)