##Ejercicio 5
"""Diseñar un algoritmo que lea del teclado dos números enteros y un carácter. El caracter puede ser +, -, *, /, %, ^, y en función 
del carácter introducido se mostrará el resultado de la operación correspondiente. Por ejemplo, si se introduce '7', '3' y '+' se mostrará 10."""


num1=int(input("Introduce un número: \n"))
num2=int(input("Introduce otro número: \n"))
correcto= True
# OPCION 1=> while accion != "+" or  accion != "-" or accion != "*" or accion != "/" or accion != "%" or accion !="**":
# OPCION 2:
while correcto == True:
   
    accion=str(input("Introduce que quieres hacer +,-,/,%,^,*: "))

    correcto  = False #Se convierte a False para que no entre bucle infinito (para que no se repita)

    match accion:
        case '+':
            print(num1+num2)
        case "-":
            print(num1-num2)
        case "*":
            print(num1*num2)
        case "/":
            print(num1/num2)
        case "%":
            print(num1%num2)
        case "^":
            print(num1**num2)
        case _:
            correcto = True
            print("Has introducido una accion invaldia.")