# Listas (Estructura ordenada para guardar elementos)
my_list = ["Mauro","Betty","Arya","Pablo"]
print(my_list)
my_list.append("Familia")  # Agregar/Insertar un elemento al final de la lista
print(my_list)
my_list.remove("Familia") #  Eliminar/Borrar un elemento de la lista
print(my_list)
print(my_list[1]) # Accedemos a una posición específica de la lista 
my_list [1] = "Bea" # Cambiamos el valor de una posición específica
print(my_list) # Imprimimos la lista modificada
my_list.sort()  # Ordenamos la lista. Por defecto lo hace alfabeticamente y si hay numeros van antes que el texto
print(my_list)
print(type(my_list))

# Tuplas (para estructuras de datos que sea inmutable (que no se cambia))
my_tuple: tuple = ("Mauro","Pereira","Ríos","@Gins","36")
print(my_tuple[2])
print(my_tuple[1:3]) # Imprime desde la posición 1 hasta la 3
print(my_tuple[1:]) # Imprime desde la posición 1 hasta el final
print(my_tuple[:3]) # Imprime desde el inicio hasta la posición 3
print(my_tuple) # Imprime la tupla completa
my_tuple = tuple(sorted(my_tuple))  # Ordena la tupla (si no ponemos tuple(sorted) se convierte en lista)
print(type(my_tuple))


# Sets {} evita duplicados. Estrucutura no ordenada pero como es rápida a la hora de buscar nos sirve para buscar elementos
my_set = {"Mauro","Pereira","Ríos","@Gins","36"} 
print(my_set)
my_set.add("mauro@gmail.com")  # Agregar/Insertar un elemento
my_set.add("mauro@gmail.com") # No nos dejaría volver a repetir el mismo add (HASH)
my_set.remove("Mauro")  # Eliminar/Borrar un elemento
print(my_set)
my_set.update #Aqui el update amplia los datos que ya tenemos en este set (concatenar)
my_set= set(sorted(my_set))
print(type(my_set))

# Diccionario:  los datos que se guardan son clave/valor
my_dict:dict = {
    "name":"Mauro",
    "surname":"Pereira",
    "surname2":"Ríos",
    "alias":"@Gins"
    ,"age":"36"
}
# Para acceder a una posición utilizamos my_dict[] y nos saldrán las opciones que hay dentro del diccionario(name,etc)
print(my_dict["name"]) # Accedemos a una posición específica del diccionario
my_dict["email"]="mauro@gmail.com" # <---- En caso de que no exista se añade de esta manera 
my_dict["age"]= "37" #  <---- En caso de que exista se modifica de esta manera [ACTUALIZACION]
del my_dict["surname"]  #  Eliminar/Borrar un elemento del diccionario
print(my_dict) # Imprimimos el diccionario completo
my_dict =  dict(sorted(my_dict.items())) # Ordena el diccionario
print(my_dict)
print(type(my_dict))

# Extra 
# Ejercicio: 
# Crea una agenda de contactos por terminal.
# - La agenda debe tener un menú con las siguientes opciones: busqueda, inserción, actualización y eliminación de contactos.
# - Cada  contacto debe tener un nombre y un número de teléfono.
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
#   solicita los datos necesarios para realizar la operación.
# - El programa NO puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
# - También se debe proponer una operación para finalización del programa
# 

def my_agenda():
    
    agenda = {}
    is_on = True
    
    def insert_contact(): # Este código se ha hecho dos veces en caso 2 y 3. Para ello y mejorar código limpio, se ha hecho esta función.
        phone = input("Introduce el nuevo número de teléfono: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <=11:
            agenda[name] = phone
        else: 
            print("Debes introducir un número de teléfono con un máximo de 11 dígitos.")
    
    while  is_on:

        print()
        print("1. Buscar contacto.")
        print("2. Insertar contacto.")
        print("3. Actualizar contacto.")
        print("4. Eliminar contacto.")
        print("5. Salir.")    
        
        option = input("Selecciona una opción: ")
        
        match option:
            case "1":
                name = input("Introduce el número de contacto a buscar: ")
                if name in agenda:
                    print(f"El número de teléfono de  {name} es: {agenda[name]}.")
                else:
                    print(f"El {name} no existe el contacto")
            case "2":
                name = input("Introduce el número de contacto: ")
                insert_contact()
            case "3":
                name = input("Introduce el número de contacto a actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"EL contacto {name} no existe o el número de teléfono no es válido.")
            case "4":
                name = input("Introduce el nombre que deseas eliminar: ")
                if name in agenda:
                    del agenda[name]
                    print("Borrado con éxito.")
                else:
                    print(f"El {name} no existe el contacto.")
            case "5":
                print("Saliendo de la agenda.")
                is_on= False
            case _:
                print("Opción inválida. Elige una opción del 1 al 5.")    
my_agenda()

