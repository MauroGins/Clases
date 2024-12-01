#Calcular la media de los números ingresados

n_vueltas = int(input("Introduce la cantidad de numeros a calcular: \n"))
contador = 0
suma = 0

while contador < n_vueltas:
    num=int(input("Introduce un valor: \n"))
    contador += 1
    suma = num + suma
    
    
media= suma /n_vueltas
    
    
print(media)