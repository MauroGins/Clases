"""
Ejercicio 17
Diseñar varias funciones para cumplir con los siguientes requisitos:

Función que lea una serie de números enteros positivos desde teclado y los almacene en una lista. # funcion1
Función que reciba una lista de enteros y devuelva la suma de los elementos. # Funcion2
Función que reciba una lista de enteros y devuelva el mayor.
Función que reciba una lista de enteros y devuelva el menor.
Función que reciba una lista de enteros y devuelva la media.
Función que reciba una lista de enteros y devuelva la mediana.
Función que reciba una lista de enteros y devuelva la varianza.
Función que reciba una lista de enteros y devuelva la desviación típica.
función que reciba una lista de enteros y devuelva si es simétrica o no.
Función que reciba una lista de enteros y devuelva si cada elemento es un número primo o no.
Función que reciba una lista de enteros y devuelva si cada elemento es un número capicúa o no.
Incluir un programa que pruebe todas las funciones.
"""

lista = []
suma = 0
mayor = 0
menor = 0
media = 0
mediana = 0
varianza = 0 


# Funcion 1
def funcion1()-> list:
    num= 0
    lista =[]

    while not num < 0:
        num= int(input("Introduce números positivos y un número negativo para salir: "))
        if not num <0:
            lista.append(num)
    return lista

# Funcion2
def funcion2(lista):
    resultado = 0
    for valor in lista:
        resultado += valor
    return resultado


def funcion3(lista):
    mayor = lista[0]
    contador= 0
    for valor in lista:
        if valor > mayor:
            mayor= valor
        contador -= 1
        if lista[contador]>mayor:
            mayor = lista[contador]
        if contador == len(lista)//2:
            return mayor
        

def funcion4(lista):
    
    menor = lista[0]
    contador= 0
    for valor in lista:
        if valor < menor:
            menor= valor

        contador -= 1
        if lista[contador] < menor:

            menor = lista[contador]
                
        if abs(contador) > len(lista)//2:
            return menor
        
prueba = [17,15,23,7,9,13]

def funcion5(lista):
    suma = funcion2(lista)
    media = suma / len(lista)
    return media

def funcion6(lista):
    lista.sort()
    mitad = len(lista)//2
    if (len(lista) % 2) == 0:
        mediana  = (lista[mitad]+lista[mitad+1]) /2
        print("par")
    else:
        mediana = lista[mitad]
        print("impar")
    return mediana

def funcion7(lista):
    media = funcion5(lista)
    paso1 = []
    paso2 = 0 
    paso3 = 0
    for valor in lista:
        paso1.append(valor - media)
    for valor in paso1:
        paso2 += valor**2

    print(paso2)
    paso3 = (paso2/len(lista)-1)**0.5
    return paso3

if __name__ == "__main__":


    lista = funcion1() 
    print(lista)
    suma=funcion2(prueba)
    print(suma)
    mayor=funcion3(prueba)
    print(mayor)
    prueba.reverse()
    menor=funcion4(prueba)
    print(menor)
    media =  funcion5(prueba)
    print(media)
    mediana = funcion6(prueba)
    print(mediana)
    varianza = funcion7(prueba)
    print(varianza)


