"""
Escribir una función que reciba un diccionario y una clave y devuelva
el valor asociado a la clave. Si la clave no existe debe devolver un mensaje de error.
"""

# Entrada de datos

prueba = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

def valor(diccionario: dict, clave: str):
    # Proceso de la función
    try:
        if not isinstance(diccionario,dict):
            raise TypeError("La entrada debe ser un diccionario")
        return diccionario[clave]
    except KeyError:
        return print(f"La clave '{clave}' no existe en el diccionario.")
    except TypeError:
        return print(f"La entrada debe ser un diccionario")
    except Exception as e:
        return print(f"Ha ocurrido un error: {e}")
    






# Salida de datos

if __name__=="__main__":
    print(valor(prueba, 'a'))  # Salida: 1
    print(valor(prueba, 'f'))  # Salida: La clave 'f' no existe
    