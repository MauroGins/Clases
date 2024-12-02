"""
Ejercicio 1
Disear una función que intercambie el valor de dos variables de tipo entero.
Incluir el algoritmo principal que realice la llamada a dicha función.
"""

def intercambio(a:int, b:int)-> tuple:
    """
    Intercambia los valores de a y b.
    """
    a,b = b,a
    return a,b

print("Intercambio sin tuplas")


def intercambioSinTuplas()-> None:
    global y
    global x
    aux = x
    x = y
    y = aux
    

if __name__==  "__main__":
    a=5
    b=10
    print(f"Antes de intercambiar: a={a}, b={b}")
    print(a,b)
    a,b = intercambio(a,b)
    print(a,b)
    
    y = 5
    x = 10
    print(x,y)
    intercambioSinTuplas()
    print(x,y)
