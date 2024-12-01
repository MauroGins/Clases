numero = int(input("Introduce el tiempo a calcular en minutos: \n"))
horas = numero //60
minutos = horas //60
suma_horas = minutos + horas
suma_minutos= minutos +  numero % 60


if suma_horas >24:
    dia = suma_horas //24
    suma_horas = suma_horas - dia * 24
    print(f"El tiempo es de {dia} dias, {suma_horas} horas y {suma_minutos} minutos")

    
   
   
else:

    print(f"El tiempo es {suma_horas} horas y {suma_minutos} minutos")

