
#Calcular la media de los números ingresados

suma = 0
cantidad_numeros = int(input("Introduce la cantidad de numeros para calcular la media"))

for i in range(cantidad_numeros):
    numero = float(input("Introduce un valor"))
    suma = suma + numero
    
    
media = suma / cantidad_numeros

print(media)

    
