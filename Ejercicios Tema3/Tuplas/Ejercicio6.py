"""
Escribir una función que reciba una tupla de números y devuelva su máximo y su mínimo.
"""

def max_min(tupla):
    try:
        return max(tupla), min(tupla)
    except TypeError:
        print( "Error: La tupla debe contener números.")
    except ValueError:
        print("Error: La tupla no puede estar vacía.")
    except Exception as e:
        print(f"Error: {e}")
    # Ejemplo de uso
    tupla = (1, 2, 3, 4, 5)
print(max_min((1, 2, 3, 4, 5)))  
print(max_min((5, 4, 3, 2, 1)))
print(max_min((1, 2, 'a', 4, 5)))
