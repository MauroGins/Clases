#Ejercicio 17

"""Diseñar un algoritmo que lea números enteros positivos de teclado y sólo acepte como válidos
aquellos que sean mayores que el anterior número leído. El algoritmo terminará cuando se introduzca el 0."""


num = -1 #Inicializas a -1 para comprobar que sea mayor y asi sabemos que son positivos

while num <0:
    num = int(input("Introduzca un número positvo: ")) #pedimos un número y comprobamos si es positivo

    if num < 0 :
        print("El número introducido no es un positivo.")
        
        
        
while num != 0: #mientras el número sea mayor que 0 y diferente a 0.
    print("Pulse 0 para salir.") 
    aux = int(input("Introduzca un número mayor que el actual:("+ str(num) + ")\n")) # pedimos un nuevo número
    
    if aux > num:
        num = aux
        
    elif aux == 0: 
        break
    
    else:
        print("El numero introducido no es mayor que el anterior")
        
        
print("Fin del programa")