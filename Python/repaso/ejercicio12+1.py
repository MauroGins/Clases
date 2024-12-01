"""/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */"""
 

# Definir una función que genere la secuencia de Fibonacci

contador = 0
a, b = 0, 1

while contador < 25:
    print(b)   
    a = a+b 
    b = a+b
    print(a)
    contador +=1