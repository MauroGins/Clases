"""
Diseñar una función que dado un número entero positivo, diga si es o no un número perfecto.
Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. 
Por ejemplo, 6 es perfecto porque sus divisores propios son 1, 2 y 3, que suman 6. Incluir 
el algoritmo principal que realice la llamada a dicha función.
"""

def perfecto(n: int) -> bool:
    """
    Esta función determina si un número 
    entero positivo es perfecto o no.
    """
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma == n
    
print(perfecto(6)) #True
print(perfecto(10)) #False
