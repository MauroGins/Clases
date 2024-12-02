#Diseñar un algoritmo que lea del teclado dos números enteros y un carácter. El caracter puede ser +, -, *, /, %, ^, y en función del carácter
#introducido se mostrará el resultado de la operación correspondiente. Por ejemplo, si se introduce '7', '3' y '+' se mostrará 10.


print("Introduce un numero ")
num1 = int(input())
print("Introduce un segundo numero ")
num2= int(input())
print("Que acción quieres hacer?+, -, *, /, %, ^")
operador = input()

match operador:
    case "+":
        print("La sumas es ",num1 + num2)
    case "-":
        print("La resta es ",num1 - num2)
    case "*":
        print("La multiplicación es ",num1 * num2)
    case "/":
        if num2 == 0:
            print("No se puede dividir por 0")
        else:
            print("La división es ",num1 / num2)
    case "%":
        if num2 == 0:
            print("No se puede dividir por 0")
        else:
            print("El resto es ",num1 % num2)
    case "^":
        print("El exponencial es ",num1 ** num2)
    case "_":
        print("Operador no válido")
    
        
