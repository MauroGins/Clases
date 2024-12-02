# Ejercicio 2

"""
Diseñar una función que tenga como entrada tres números enteros y nos devuelva el mayor de los tres.
Incluir el algoritmo principal que realice la llamada a dicha función.
"""

def enteros(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 <=1 and num2 >=num3:
        return num2
    else:
        return num3


if __name__=="__main__":
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
    print(f"El numero mayor de los 3 es: {enteros(num1,num2,num3)}")
    
