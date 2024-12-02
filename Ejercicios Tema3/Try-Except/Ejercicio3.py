"""
Escribir una función que reciba una cadena y un número n y devuelva la cadena
repetida n veces. Si el número es negativo debe devolver un mensaje de error.
"""

# Entrada de datos

def repetir_cadena(cadena,n):
    try:
        return cadena * n
    except TypeError:
        print( "Error: El número debe ser un entero o un número flotante")
    except ValueError:
        print( "Error: El número debe ser un entero o un número flotante")
    


# Salida de datos

if __name__=="__main__":
    cadena = input("Introduce una cadena de texto: ")
    n= int(input("Introduce el número de veces que quieres que se repita la cadena "))
    resultado = repetir_cadena(cadena, n)
    print(resultado)
    
