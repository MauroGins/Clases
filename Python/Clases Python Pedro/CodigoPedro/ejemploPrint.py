
edad = int(input("Introduce la edad: "))
nombre = input("Introduce nombre: ")

#unicamente mostrar el valor de la variable
print(edad)

#mostrar mensaje y valor de la variable
print("La edad es:", edad)
print("La edad es: " + str(edad))
print(f"La edad es: {edad}")

#mostrar más de un mensaje y más de una variable
print("El alumno se llama", nombre, "y tiene", edad, "años")
print("El alumno se llama " + nombre + " y tiene " + str(edad) + " años")
print(f"El alumno se llama {nombre} y tiene {edad} años")