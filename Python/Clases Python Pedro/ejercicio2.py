"""
Calcular la distancia entre dos puntos x e y en un plano y que muestre por pantalla la distancia que existe entre ellos.
A(x1,y1) B(x2,y2)
"""
import math
#Las librerias se pueden renombrar.  Por ejemplo > import math as m < y pasaría a llamarse m.


#DATOS DE ENTRADA
#Pedimos las coordenadas de dos puntos (x1,y1) (x2,y2)
x1= float(input("Ingrese la coordenada x del primer punto:"))
y1= float(input("Ingrese la coordenada y del primer punto:"))

x2= float(input("Ingrese la coordenada x del segundo punto:"))
y2= float(input("Ingrese  la coordenada y del segundo punto:"))

#PROCESAR LA INFORMACIÓN
#Calculamos la distancia entre los puntos usando la fórmula [SIN LIBRERIAS]

distancia = ((x2-x1)**2 + (y2-y1)**2 )**0.5

#MOSTRAR EL RESULTADO
print("La distancia entre los puntos es:", distancia)  #Mostramos la distancia entre los dos puntos


#Con libreria, <<import math>>

distancia = math.sqrt(math.pow(x2-x1,2)+ math.pow(y2-y1,2))
print("La distancia entre los puntos es:", round(distancia,2))  #Mostramos la distancia entre los dos puntos
