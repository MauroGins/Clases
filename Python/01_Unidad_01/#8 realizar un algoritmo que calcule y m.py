#8 realizar un algoritmo que calcule y muestre
# en la pantalla la suma de los n primeros enteros impares.
# El valor de n se solicitará al usuario.


n=int(input("Dame numero: "))
resultado = 0
for i in range(1,n+1,2):
    resultado = resultado + i 
    print(i)
    print("----")
 



print("--------------------------------------------------")

resultado2= 0

for i in range(1,n+1):
    if i % 2 == 0: #esto dice que es PAR "i" por que su resto es 0
        resultado2= resultado2 + i
   
print(resultado2)