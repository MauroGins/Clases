"""
Escribe un programa que reciba dos números naturales y determina cual
es múltipolo del otro. Si no son múltiplos también se debe indicar
"""

#ENTRADA DE DATOS
#pedir al usuario los dos números

num1=int(input("Introduce número 1: "))
num2=int(input("Introduce número 2: "))


#PROCESO
#comprobar si el primer número es múltiplo del segundo
#num1 es múltiplo de num2 cuando el resto de la division num1%num2==0
if num1%num2==0:
    print(f"El número {num1} es múltiplo del número {num2}")
elif num2%num1==0:
    print(f"El número {num2} es múltiplo del número {num1}")
else:
    print(f"Los números {num1} y {num2} no son múltiplos entre sí")
