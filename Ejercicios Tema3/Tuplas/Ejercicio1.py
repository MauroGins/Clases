"""
Escribir una función que reciba una tupla de elementos e indique si se encuentran ordenados de menor a mayor o no.
"""

tuplaEntrada=(1,6, 3, 4, 5,3,8)
tuplaEntrada2=(1,2,3,4,5,6)

# Entrada de datos

def ordenar(tupla:tuple):
    try:
        tupla2 = list(tupla)
        # Comprobamos si la tupla está ordenada de menor a mayor
        if tupla == tuple(sorted(tupla2)):
            return True
        else:
            return False
    except TypeError:
        print("Error: La tupla debe contener elementos comparables")
    except Exception as e:
        print(f"Error: {e}")
        


# Salida de datos

if __name__=="__main__":
    print(ordenar(tuplaEntrada2))