"""
Escribir una función que reciba una tupla de números y un valor n y
devuelva una lista con los elementos de la tupla que son múltiplos de n.
"""
multiplos=(1,2,3,4,5)
def multiplos(tupla:tuple,n:int) -> list:
    try:
        return[i for i in tupla if i % n==0]
    except TypeError:
        print("Error: la tupla debe contener solo números")
    except ZeroDivisionError:
        print("Error: n no puede ser cero")
    except Exception as e:
        print(f"Error: {e}")
        

print(multiplos(1,2,3,4,5),2)