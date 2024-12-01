#Ejercicio 1
"""Diseñar un algoritmo que convierta una temperatura leída en 
grados Farenheit a grados Celsius, usando la fórmula: C=(5/9)*(F-32)."""





what =""

while what != "F" and what !="C":
    
    what=str(input("A que quieres convertir la temperatura? (F) para Farenheit o a (C) para Celsius:\n "))
    
    if what =="F":
        temp=float(input("Introduce una temperatura en Farenheit:\n "))
        convers=(5/9)*(temp-32)
        print(f"La temperatura {temp} F es igual a {convers}ºC.\n")
    elif  what=="C":
        temp=float(input("Intorduce una temperatura en Celsius:\n "))
        convers=(temp*9/5)+32
        print(convers)
    else:
        print("No es una opción:\n")

