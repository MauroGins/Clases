"""
Escribir una función que reciba dos números y devuelva su división.
Si el segundo número es cero debe devolver un mensaje de error.
"""
num1=0
num2=0

# Proceso de la función

def div(num1,num2):
    
    # Entrada de datos 
    
    global division
    try:     
        num1=float(input("Introduce un número uno: "))
        num2=float(input("Introduce un número dos: "))
        division=(num1/num2)
        return division
    
    except ValueError:
        print("ERROR: El valor introducido no es un número.")
        
    except ZeroDivisionError:
        print("ERROR: El número dos no puede ser 0.")
        
    except Exception as e:
        print("ERROR: ", str(e))


# Salida de datos

if __name__=="__main__":
    print("El resultado de la división es:",div(num1,num2))  

