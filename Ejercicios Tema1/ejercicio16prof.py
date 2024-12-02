""""Solución  Ejercicio 16 profesor""" 


print("--------------------------------------------------")


#versión sencilla y de andar por casa

num = int(input("Introduce un número del 1/9: "))

if num <1  or num >9:
    print("Número no válido")
elif num == 1 or num == 4  or num == 6 or num == 8:
    print(f"El {num} no es primo")
else: 
    print("Es primo")


#Versión para cualquier número

print("--------------------------------------------------")


for i in range(2,num): #bucle para comprobar si es primo
    if num % i == 0: #si el número es divisible por i
        print("No es primo.")
        break #Salimos del bucle.
else:
    print("Es primo.")
    
    
#Versión con while

print("--------------------------------------------------")

i=2 #inicializamos  el bucle con 2

while i< num: #mientras el divisor sea menor  que el número
    if num % i == 0: #si el número es divisible por i
        print("No es primo.")
        break #Salimos del bucle.
    i +=1 #incrementamos el divisor

else: 
    print("Es primo.")
    

