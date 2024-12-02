"""
Diseñar una función que permita calcular el número e, o número de Euler,
mediante la siguiente serie infinita: e = 1 + 1/1! + 1/2! + 1/3! + 1/4! + ...
para una precisión dada por el usuario, la precisión indicará las vueltas que
debe dar el algoritmo a la serie infinita. Incluir el algoritmo principal que
realice la llamada a dicha función. Como paso previo, se puede diseñar una función 
que calcule el factorial de un número entero.
"""
import math

def euler(num:int):
    """Calcula el número e mediante la serie infinita: e = 1 + 1...
    """
    e = 0
    for i in range(num):
        e += 1 / math.factorial(i)
        return e
    return e


    
    
    
if __name__=="__main__":
    print(euler(1))