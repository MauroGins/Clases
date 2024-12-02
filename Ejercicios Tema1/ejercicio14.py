"""Diseñar un algoritmo que calcule la potencia para dos 
números naturales x e y mediante una acumulación sucesiva de productos.
Previo al cálculo se verificará que ambos valores son positivos."""


x_potencia = int(input("Introduce el valor de X :"))
y_potencia = int(input("Introduce el valor de y :"))

if x_potencia > 0 and y_potencia > 0: 

    dif_potencias = x_potencia ** y_potencia
    print(f"La potencia de {x_potencia} elevado a la {y_potencia} es {dif_potencias}")
else:   
    print("No puedes ejecutar el programa con valores negativos o menores que 0")
