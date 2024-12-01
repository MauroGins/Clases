#Un programa que compruebe si el numero es primo o no 


numero = int(input("Introduce un numero para comprobar si es primno o no: \n > "))

controlador= False

if numero > 2:
    for i in range(2,numero-1):
        if(numero % i) == 0: 
            controlador = True
    if controlador == True:
        print(f"El numero {numero} no es primo")
    else: 
        print(f"El número {numero} es primo")
elif numero == 2:
    print("El numero es primo")           
else: 
    print("No se acepta ese valor")