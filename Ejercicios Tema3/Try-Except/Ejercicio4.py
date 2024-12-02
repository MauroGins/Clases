"""
Escribir una función que reciba una lista de números y devuelva
una lista con los cuadrados de los números. Si la lista contiene 
algún elemento que no es un número debe devolver un mensaje de error.
"""

# Entrada de datos

lista = [1,2,"a",4,5]


def cuadrados(lista):
    try:
        
        for i in lista:
            if not isinstance(i, (int, float)):
                raise TypeError("La lista contiene elementos que no son números")
            else:            
                cuadrado = i**2
            print(cuadrado)
            
        return lista
    except TypeError:
        print("Error: La lista contiene elementos que no son números")
    except: 
        print("Error inesperado.")



# Salida de datos

if __name__=="__main__":
    cuadrados(lista)
    
    