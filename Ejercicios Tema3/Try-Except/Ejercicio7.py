"""
Escribir una función que reciba una lista de números y devuelva el número más grande.
Si la lista está vacía debe devolver un mensaje de error.
"""
lista = [1, 2, 7, 4, 5]
# Entrada de datos

def nombre(lista:list):
    
    try:
        if len(lista) == 0:
            return print("La lista está vacía")
        else:
            return max(lista)
    except ValueError:
        return print("Error: La lista debe contener números")
    except TypeError:
        return print("Error: La lista no puede contener strings")
    except Exception as e:
        return print(f"Error: {e}")
    

# Salida de datos

if __name__=="__main__":
    print(nombre(lista))