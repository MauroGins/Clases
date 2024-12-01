"""
Funciones definidas por el usuario
"""
#Simple

def saludo():
    print("Hola, Python!")
    
saludo()

# Con retorno

def return_greet():
    return "Hola, Python!"

greet = return_greet() #guardas o no el retorno en una variable.
print(greet)
print(return_greet())

# Funciones con un argumento.

def arg_greet(name):
    print(f"Hola, {name}!")
    
arg_greet("Mauro")  #Puedes pasar cualquier tipo de dato.

# Funciones con argumentos.

def args_greet(greet,name):
    print(f"{greet} {name}!")
    
args_greet("Hi","Mauro")  #Puedes pasar cualquier tipo de dato.

# Funcion con argumento predeterminado.

def default_arg_greet(name="Python"):
    print(f"Hi, {name}!")

default_arg_greet() #Aqui coge el argumento name=Pyton por defecto
default_arg_greet("Mauro") #Aqui puedo darle o no un retorno

# con posicionamiento

def args_greet(greet,name):
    print(f"{greet} {name}!")
    
args_greet("Hi","Mauro")  #Puedes pasar cualquier tipo de dato.
args_greet("Mauro","Hi") # así los desordena
args_greet(name="Mauro", greet="Hi") # Aunque se los demos desordenados nos los ordena por que estoy definiendo que es cada String.

#Con argumentos y retorno

def return_args_greet(greet, name):
    return f"{greet}, {name}!"

print(return_args_greet("Hi","Mauro"))

#Con retorno de varios valores

def multiple_return_greet():
    return "Hi","Mauro","Galicia"

greet, name, place = multiple_return_greet()
print(greet)
print(name)
print(place)

#Con un numero variable de argumentos


def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")
        
variable_arg_greet("Python","Mauro","Bea","Pablo",)

#Con un número variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key,value in names.items():
        print(f"Hola, {value}, ({key})!")
        
variable_key_arg_greet(
    tipo_rel="Realcion",
    nombre="Mauro",
    nombre1="Bea",
    tipo="Esposa",
    tiempoJuntos=6
)

# Funciones dentro de funciones

def outer_function():
    def inner_function():
        print("Funcion interna: Hola, Python")
    inner_function()   
        
outer_function()

# Funciones de lenguaje (built-in function) 

print() #este es un ejemplo
print(len("Mauro")) #Es una funcion que cuenta  el numero de caracteres de una cadena de texto
print(type("Mauro")) #tipo
print(("Mauro".upper())) #tipo

# Variables locales y globales

global_variable = "Python"
print(global_variable)

def hello_python():
    print(f"Hello, {global_variable}!")
    
hello_python()

global_var="Python"

print(global_var)

def hello_python():
    local_var="Hola"
    print(f"{local_var}, {global_var}")
    
hello_python() 
print(global_var)
##  print(local_var)    # Está definida dentro de la funcion por eso no podemos hacer la llamada a la variable.

                    # Si intentamos hacer la llamada a la variable local_var fuera de la funcion, nos dara
                    # error porque no está definida en ese contexto.

#Extra ejercicio tipo Fizz Buzz

def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2) 
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else: 
            print(number)
            count += 1
        return count
print(print_numbers("Fizz","Buzz"))