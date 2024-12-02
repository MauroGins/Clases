"""
Escribir una función que reciba una lista de números y devuelva su media.
Si la lista está vacía debe devolver un mensaje de error.
"""


# Entrada de datos

lista_numeros=[]

def media(lista_numeros):
    try:
    # Verificar si la lista está vacía
        if len(lista_numeros) == 0:
            return None
        else:
            # Calcular la media
            media = sum(lista_numeros) / len(lista_numeros)
            return media
    except ValueError:
        print("ERROR:La lista está vacía")
    except ZeroDivisionError:
        print("ERROR:No se puede dividir por cero")
    except:
        print("ERROR:Ocurrió un error inesperado")



# Salida de datos
if __name__=="__main__":
    print(media(lista_numeros))
    
