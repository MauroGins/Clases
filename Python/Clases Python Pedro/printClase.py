edad = int(input("Introduce la edad: "))
nombre = input("Introduce nombre del alumno:")

#Muestra unicamente el valor de la variable
print(edad)

#Muestra el mensaje y valor de la variable.
print("La edad es:",edad)

#Ahora concatenando la variable
print("La edad es: " + edad) 
#Error: No se puede concatenar STRING + INT
#Se soluciona convirtiendo a string
print("La edad es: " +str(edad))

#Muestra más de un mensaje y más de una variable
print("El alumno se llama", nombre, "y tiene", edad,"años")
print("El alumno se llama "+ nombre+ " y tiene"+ str(edad)+ " años")

#Con funcion de escritura
print(f"El alumno se llama {nombre} y tiene {edad} años")