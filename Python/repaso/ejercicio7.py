numero = int(input("Introduce un número a calcuar: \n"))

factorial = 1
contador = 1

while contador <= numero:
    factorial = factorial * contador
    contador +=1
    
    
print(factorial)
