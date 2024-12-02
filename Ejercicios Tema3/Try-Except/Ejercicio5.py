"""
Escribir una función que reciba una tupla y una posición y devuelva el elemento
de la tupla en la posición indicada. Si la posición es mayor que la longitud de
la tupla debe devolver un mensaje de error.
"""
# Entrada de datos

tupla = ('a', 'b', 'c', 'd')
print(type(tupla))
p = 2

# Proceso de datos

def position(tupla,p):
    try:
        if p < len(tupla):
            return tupla[p]
        
    except TypeError:
        print("Error: La tupla no es una tupla")
    except Exception as e:
        print(f"Error: {e}")
    except:
        print("Error: La posición indicada es mayor que la longitud de la tupla")

# Salida de datos

if __name__=="__main__":
    print(f"La posición {p} es:",position(tupla,p))