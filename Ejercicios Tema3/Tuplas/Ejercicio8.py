"""
Escribir una función que reciba una tupla de números y devuelva la tupla con sus elementos ordenados de menor a mayor.
"""

# Entrada de datos

def ordenar_menor_mayor(tupla: tuple):
    try:    
    # Proceso de ordenamiento
        tupla_ordenada = sorted(tupla)
        return tupla_ordenada
    except TypeError:
        print("Error: La tupla debe contener solo números enteros o flotantes")
    except Exception as e:
        print("Error: ", str(e))
        
# Prueba de la función
print(ordenar_menor_mayor((5, 2, 8, 1)))
print(ordenar_menor_mayor((10, 7, 3, 9)))
print(ordenar_menor_mayor((4, 6, 2, 8)))
print(ordenar_menor_mayor((1, 3, 5, 7)))
