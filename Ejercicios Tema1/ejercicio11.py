"""Diseñar un algoritmo que lea del teclado un número entero correspondiente a una cantidad de minutos y nos diga cuántos días, horas y minutos son. 
Por ejemplo, si introducimos 1000 minutos, el algoritmo mostrará por pantalla que son 0 días, 16 horas y 40 minutos."""

print("Que cantidad de minutos desdeas calcular?")

cantidad = int(input())

cantidad_dias = cantidad // 1440
cantidad_minutos =  cantidad % 14400
cantidad_horas = cantidad_minutos // 60
cantidad_minutos = cantidad_minutos % 60
print(cantidad_dias,"día/s",cantidad_horas,"horas",cantidad_minutos,"minutos")





"""Resuelto por el profesor"""
print("-------------PROFESOR-----------------")



minutos = input("introduce los minutos: ")

if minutos.isdigit():
    minutos = int(minutos)
    horas = minutos // 60
    minutos = minutos % 60
    dias = horas // 24
    minutos = horas % 24
    print(f"Son {dias} dias, {horas} horas y {minutos} minutos")
else:
    print("Error, no es un número")