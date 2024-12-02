##Ejercicio 16
"""
Diseñar un algoritmo que pida al usuario un número del 1 al 9
y le conteste diciendo si el número es primo o no. Por ejemplo,
si el usuario introduce el número 7, el algoritmo le responderá que
7 es un número primo.
"""

num_introducido = int(input("Introduce un valor del 0-9: \n"))
n= num_introducido

def is_prime(n):

    if n <= 1:

        return False

    for i in range(2, int(n**0.5) + 1):  #

        if n % i == 0:

            return False

    return True




if is_prime(n):

    print(f"El {n} es un número primo")

else:

    print(f"El {n} no es un número primo")
    
    
