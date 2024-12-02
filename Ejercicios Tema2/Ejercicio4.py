# Ejercicio 4
"""
Diseñar una función que admita, como parámetro de entrada, un caracter y que devuelva, 
como salida, el número de veces que aparece dicho carácter en una secuencia de caracteres 
leída de teclado. La secuencia de caracteres finalizará cuando el usuario introduzca un punto.
"""


def numVeces(caracter:str) -> int:
    """
    Esta función cuenta el número de veces que aparece un caracter en una secuencia de caracteres le
    ida de teclado.
    """
    # Inicializar un contador para el caracter
    contador = 0
    # Leer la secuencia de caracteres
    secuencia = input("Ingrese una secuencia de caracteres (punto para finalizar): ")
    # Mientras la secuencia no sea un punto
    if secuencia  != ".":
        # Contar el caracter en la secuencia
        contador = secuencia.count(caracter)
