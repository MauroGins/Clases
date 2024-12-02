"""
Escribir una función que reciba una tupla de números y devuelva su media y su varianza.
"""

def media_y_varianza(tupla):
    try:    
        media = sum(tupla) / len(tupla)
        varianza = sum((x - media) ** 2 for x in tupla)
        return media, varianza
    except ZeroDivisionError:
        print("Error:La tupla no puede estar vacía")
    except TypeError:
        print("Error:La tupla tiene que contener solo números")
    except Exception as e:
        print("Error:", e)
    # Ejemplo de uso
tupla = (1, 2, 3, 4, 5)
media, varianza = media_y_varianza(tupla)
print(f"Media: {media}, Varianza: {varianza}")
