#Ejercicio 4
"""Diseñar un algoritmo que lea 20 caracteres de teclado y 
muestre por pantalla el número de veces que se repiten cada una de las vocales."""



cont_vocal=0
sumaA=0
sumaE=0
sumaI=0
sumaO=0
sumaU=0
for i in range(20):
    letra = str(input(f"Introduce el caracter {i}: \n"))
    cont_vocal +=1
    
    match letra:
        case "a"|"A":
            sumaA=sumaA+1
        case "e"|"E":
            sumaE=sumaE+1
        case "i"|"I":
            sumaI=sumaI+1
        case "o"|"O":
            sumaO=sumaO+1
        case "u"|"U":
            sumaU=sumaU+1
        
print(f"Total de la suma de vocales:\nA:{sumaA} \nE:{sumaE} \nI:{sumaI} \nO:{sumaO} \nU:{sumaU}")
