#Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres en tu lenguaje.
#Algunas de esas operaciones podrían ser (busca todas las que puedas):
#   -Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
#       conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación,...

"""
Operaciones
"""
s1 = "Hola"
s2 = "Python"

# Contatenación
print(s1+ ", " +s2+"!")

# Repetición
print(s1*3)

# Indexación
print(s1[0]+s1[1]+s1[2]+s1[3])

# Longitud
print(len(s2))

# Slicing (porción)
print(s2[2:5]) #Siendo 2 índice inicial y 5 como índice final "tho" 
print(s2[2:]) #Así empieza en 2 y llega al final
print(s2[:5]) #Así llega al 5  y empieza en 0

# Búsqueda [Retorna True/False]
print("a" in s1)
print("i" in s1)

#  Reemplazo [Cambiaría la letra o de la cadena s1 por la a]
print(s1.replace("o","a"))

#  División 
print(s2.split("t")) #Corta la cadena por cada caracter "t" [la t desaparecería]

# Mayúsculas y minúsculas
print(s1.upper()) #Reporta mayúsculas
print(s1.lower()) #Reporta minúsculas
print("mauro ríos".title()) #Reporta la cadena de caracteres  con la primera letra de cada palabra en mayúscula y el resto en minúsculas
print("mauro ríos".capitalize())  #Reporta la cadena de caracteres con SOLO la primera letra de la primera palabra en mayúsculas.

# Eliminación de espacios al principio y al final
print("   Mauro Ríos   ".strip() + "@maurodev") #Reporta la cadena de caracteres sin espacios (del principio y final)

# Búsqueda al principio y al final [Retorna True/False]
print(s1.startswith("Ho"))
print(s1.startswith("Py"))
print(s1.endswith("la"))
print(s1.endswith("thon"))

s3="Mauro Pereira Ríos"

# Búsqueda de posición
print(s1.find("o"))
print(s3.find("Ríos"))  #Nos retorna la posición donde EMPIEZA la cadena de caracteres "Ríos" en la 
                        # cadena de caracteres "Mauro Pereira Ríos" [14] CASE SENSITIVE
print(s3.find("mauro"))   # Nos retorna -1 ya que no hay nada que empiece en mínusculas                                         
print(s3.lower().find("mauro"))   # Nos retorna la posición donde está "mauro" en minúsculas en la cadena de caracteres.[0]

# Búsqueda de ocurrencias 
print(s3.lower().count("m")) # Cuenta cuantas veces aparece la letra "m" en minúsculas en la cadena de caracteres s3 [se puede buscar palabra]

# Formateo 
print("Saludo: {}, lenguaje: {}!".format(s1,s2))

# Interpolación
print(f"Saludo: {s1}, lenguaje: {s2}!")

# Transformación en lista de caracteres
print(list(s3)) # Crea una lista con todos los caracteres de una cadena de texto

# Transformación de una lista en cadena
l1=[s1,", ",s2, "!"] # Crea una lista con una cadena de texto y un caracter
print("".join(l1)) # Poniendo las "" es el caracter que se va a usar para unir la lista de caracteres en una cadena de texto (en blanco)

# Transformaciones numéricas
s4= "1234567890"
s4= int(s4)
print(s4)

s5= "1234567890.123"
s5= float(s5)
print(s5)

# Comprobaciones varias
s4= "1234567890"    # Volvemos a typar a string 
print(s1.isalpha()) # Comprueba si la cadena de caracteres es alfanumérica
print(s1.isalpha()) # Comprueba si la cadena es de solo letras
print(s4.isalpha()) # Ahora no peta al volver a typar s4 a string
print(s4.isnumeric()) # Comprueba si la cadena de caracteres es numerica
print(s4.isdigit()) # Comprueba si la cadena de caracteres es numérica

"""
Extra:
"""
#Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son:
#   -Palíndromos
#   -Anagramas
#   -Isogramas

