# Listas en python

# Definición
# Una lista es una colección ordenada de elementos.  Pueden ser de cualquier tipo de dato. Es ordenada pero lo introducido no tiene por que seguir un orden
# Las listas se pueden crear de varias maneras:
    # 1. Usando corchetes: [1, 2, 3,]
    # 2. Usando la función list(): list([1, 2, 3])
    # 3. Usando la función range(): list(range(1, 10))
    # 4. Usando la función len(): list(range(1, len([1,])
# Una lista se define utilizando corchetes [].
# Una lista puede contener cualquier tipo de elemento.
# Una lista puede contener elementos duplicados.
# Una lista puede contener elementos de diferentes tipos.
# Una lista puede contener listas o cualquier otro tipo de colección.

# Ejemplo
print("*********************** EJEMPLO 1 **********************************")

lista = [1, 2, 3, 4, 5]
print(lista)

# Acceso a los elementos de una lista

# Los elementos de una lista se acceden utilizando un índice.
# Los índices de una lista empiezan en 0.
# Los índices de una lista son números enteros.
# Los índices de una lista pueden ser positivos o negativos.
# Los índices de una lista pueden ser variables.

# Ejemplo
print("*********************** EJEMPLO 2 **********************************")
lista = [1, 2, 3, 4, 5]
print("Primer elemento:", lista[0])
print("Segundo elemento:", lista[1])
print("Tercer elemento:", lista[2])
print("Cuarto elemento:", lista[3])
print("Quinto elemento:", lista[4])
print("Último elemento:", lista[-1]) # Quinto y último se puede acceder de las dos formas -1 o la posición que corresponda [4] en este caso.
print("Penúltimo elemento:", lista[-2])

# Modificación de los elementos de una lista

# Los elementos de una lista se pueden modificar utilizando un índice.
# Los elementos de una lista se pueden modificar utilizando un rango de índices.
# Los elementos de una lista se pueden modificar utilizando un índice negativo.
# Los elementos de una lista se pueden modificar utilizando un índice variable.

# Ejemplo
print("*********************** EJEMPLO 3 : Modificaciones **********************************")

lista = [1, 2, 3, 4, 5]
print("Lista original:", lista)
lista[0] = 10
lista[1:3] = [20, 30] # el 3 es valor limite y lo excluye. Va de 1 a 2 pero se expresa con 1:3 y lo exlcuye.
lista[-1] = 50
print("Lista modificada:", lista)

# Eliminación de elementos de una lista

# Los elementos de una lista se pueden eliminar utilizando la instrucción del.
# Los elementos de una lista se pueden eliminar utilizando un índice.
# Los elementos de una lista se pueden eliminar utilizando un rango de índices.
# Los elementos de una lista se pueden eliminar utilizando un índice negativo.
# Los elementos de una lista se pueden eliminar utilizando un índice variable.

# Ejemplo
print("*********************** EJEMPLO 3 : Deletes **********************************")

lista = [1, 2, 3, 4, 5]
print("Lista original:", lista)
del lista[0]
print("Lista modificada tras eliminar el elemento 0:", lista)
del lista[1:3] #Igual que antes, el 3 no está incluido.
print("Lista modificada tras eliminar los elementos 1 y 2:", lista)
del lista[-1]
print("Lista modificada tras eliminar el último elemento:", lista)
print("Lista modificada:", lista)

# Añadir elementos a una lista

# Los elementos se pueden añadir a una lista utilizando el método append.
# Los elementos se pueden añadir a una lista utilizando el método insert.
# Los elementos se pueden añadir a una lista utilizando el método extend.
# Los elementos se pueden añadir a una lista utilizando el operador +.
# Los elementos se pueden añadir a una lista utilizando el operador *.

# Ejemplo
print("*********************** EJEMPLO 4: Add **********************************")

lista = [1, 2, 3, 4, 5]
print("Lista original:", lista)
lista.append(6) #append añade al final
print("Lista modificada tras añadir el elemento 6:", lista)
lista.insert(0, 0) #Insert añade  en la posición indicada
print("Lista modificada tras añadir el elemento 0 en la posición 0:", lista)
lista.extend([7, 8, 9]) #hace lo mismo que append (añade al final)  pero con una lista y la concatena
print("Lista modificada tras añadir los elementos 7, 8 y 9:", lista)
lista = lista + [10]
print("Lista modificada tras añadir el elemento 10:", lista)
lista = lista * 2
print("Lista modificada tras duplicar los elementos:", lista) #Duplica los elemento de la lista


# Recorrer los elementos de una lista

# Los elementos de una lista se pueden recorrer utilizando un bucle for.
# Los elementos de una lista se pueden recorrer utilizando un bucle while.
# Los elementos de una lista se pueden recorrer utilizando un índice.
# Los elementos de una lista se pueden recorrer utilizando un rango de índices.
# Los elementos de una lista se pueden recorrer utilizando un índice negativo.
# Los elementos de una lista se pueden recorrer utilizando un índice variable.

# Ejemplo
print("*********************** EJEMPLO 5: Recorrer listas **********************************")

lista = [1, 2, 3, 4, 5]

print("Recorrido con un bucle for:")
for elemento in lista:
    print(elemento)

print("Recorrido con un bucle while:")
i = 0
while i < len(lista):
    print(lista[i])
    i += 1

print("Recorrido con un índice:")
for i in range(len(lista)):
    print(lista[i])

print("Recorrido con un rango de índices:")
for i in range(1, 4):
    print(lista[i])

print("Recorrido con un índice negativo:")
for i in range(-1, -4, -1):
    print(lista[i])

print("Recorrido con un índice variable:") #Solo para posiciones específicas
for i in [0, 2, 4]:
    print(lista[i])
    
# Métodos de las listas

# Los métodos de las listas son funciones que se pueden utilizar para realizar operaciones con las listas.
# Los métodos de las listas se utilizan con la notación de punto.
# Los métodos de las listas se utilizan con paréntesis.
# Los métodos de las listas pueden tener parámetros.
# Los métodos de las listas pueden devolver un valor.

# Ejemplo
print("*********************** EJEMPLO 6: Metodos **********************************")

lista = [1, 2, 3, 4, 5]

print("Longitud de la lista:", len(lista))

print("Número de veces que aparece el 3 en la lista:", lista.count(3)) # Cuantas veces sale el elemento en la lista

print("Índice de la primera aparición del 3 en la lista:", lista.index(3)) # Me dice la posicion de la primera aparicion de lo que le pides

lista.reverse()
print("Lista invertida:", lista)

lista.sort()
print("Lista ordenada:", lista)

lista.clear()
print("Lista vacía:", lista)


# Listas que apuntan al mismo objeto  [Alias]

# Si se asigna una lista a otra variable, ambas variables apuntan al mismo objeto.
# Si se modifica una lista, la otra lista también se modifica.
# Si se elimina una lista, la otra lista también se elimina.

# Ejemplo
print("*********************** EJEMPLO 6: Alias **********************************")

lista1 = [1, 2, 3, 4, 5]
lista2 = lista1
print("Lista 1:", lista1)
print("Lista 2:", lista2)
lista1[0] = 10
print("Lista 1 modificada:", lista1)
print("Lista 2 modificada:", lista2)
del lista1
print("Lista 2 eliminada:", lista2)

# Copia de listas

# Si se quiere copiar una lista, se puede utilizar el método copy.
# Si se quiere copiar una lista, se puede utilizar el método list.
# Si se quiere copiar una lista, se puede utilizar el operador [:].
# Si se quiere copiar una lista, se puede utilizar el método deepcopy.

# Ejemplo
print("*********************** EJEMPLO 7: Copias **********************************")

lista1 = [1, 2, 3, 4, 5]
lista2 = lista1.copy()
lista3 = list(lista1)
lista4 = lista1[:]
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3:", lista3)
print("Lista 4:", lista4)
lista1[0] = 10
print("Lista 1 modificada:", lista1)
print("Lista 2 modificada:", lista2)
print("Lista 3 modificada:", lista3)
print("Lista 4 modificada:", lista4)

# Rebanadas de listas o slices (sublistas)

# Una rebanada de una lista es una sublista de la lista original.
# Una rebanada de una lista se define utilizando un rango de índices.
# Una rebanada de una lista se define utilizando un índice inicial y un índice final.
# Una rebanada de una lista se define utilizando un índice inicial, un índice final y un paso.
# Una rebanada de una lista se define utilizando un índice inicial, un índice final y un índice negativo.
# Una rebanada de una lista se define utilizando un índice inicial, un índice final y un índice variable.

# Ejemplo
print("*********************** EJEMPLO 8: Slices (Rebanadas) **********************************")

lista = [1, 2, 3, 4, 5]

print("Rebanada de la lista:", lista[1:4])
print("Rebanada de la lista:", lista[:3]) #Todos los elemento desde  el principio hasta la posicion 3(excluida)
print("Rebanada de la lista:", lista[2:]) #Empieza en el elemento 2(inlcuido) hasta el final
print("Rebanada de la lista:", lista[::2]) #Empieza en el elemento 0(inlcuido) y salta 2 elementos
print("Rebanada de la lista:", lista[::-1]) #Invierte el orden de la lista
print("Rebanada de la lista:", lista[1:4:2])  #Empieza en el elemento en posicion 1(inlcuido) va hasta el elemento en posicion 4(exlcuido) saltando de 2 en 2 elementos

# Operadores in y not in

# El operador in se utiliza para comprobar si un elemento está en una lista.
# El operador not in se utiliza para comprobar si un elemento no está en una lista.
# Retorna verdadero o falso
# Ejemplo
print("*********************** EJEMPLO 9: in - not in **********************************")

lista = [1, 2, 3, 4, 5]

print("El 3 está en la lista:", 3 in lista)
print("El 6 no está en la lista:", 6 not in lista)

# Operadores + y *

# El operador + se utiliza para concatenar dos listas.
# El operador * se utiliza para repetir una lista un número determinado de veces.

# Ejemplo
print("*********************** EJEMPLO 10: Concatenar o repetir **********************************")

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print("Concatenación de listas:", lista1 + lista2)
print("Repetición de una lista:", lista1 * 3)

# Listas por comprensión

# Una lista por comprensión es una forma de crear una lista utilizando una expresión.
# Una lista por comprensión se define utilizando corchetes [].
# Una lista por comprensión se define utilizando una expresión seguida de una o más cláusulas for.
# Una lista por comprensión se puede utilizar para filtrar los elementos de una lista.
# Una lista por comprensión se puede utilizar para transformar los elementos de una lista.
# Una lista por comprensión se puede utilizar para combinar los elementos de dos o más listas.

# Ejemplo
print("*********************** EJEMPLO 11: Compresión **********************************")
print()
lista = [1, 2, 3, 4, 5]

pares = [numero for numero in lista if numero % 2 == 0]
cuadrados = [numero ** 2 for numero in lista]
combinada = [(numero, numero ** 2) for numero in lista]

print("Lista original:", lista)
print("Lista de pares:", pares)
print("Lista de cuadrados:", cuadrados)
print("Lista combinada:", combinada) # Lista de tuplas

# Listas y cadenas de texto

# Una cadena de texto se puede convertir en una lista utilizando el método split.
# Una cadena de texto se puede convertir en una lista utilizando el método list.
# Una cadena de texto se puede convertir en una lista utilizando el operador [].
# Una cadena de texto se puede convertir en una lista utilizando una lista por comprensión.

# Ejemplo
print("*********************** EJEMPLO 12: Listas y cadenas **********************************")
print()
cadena = "Hola, mundo!"
lista1 = cadena.split()  #separamos la cadena en una lista. Lo que se pase como parametro es el separador que queremos tener para la lista.
lista2 = list(cadena)   #convertimos la cadena en una lista.
lista3 = [caracter for caracter in cadena]   #convertimos la cadena en una lista mediante compresión.


print("Cadena original:", cadena)
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3:", lista3)

# Listas anidadas

# Una lista anidada es una lista que contiene otras listas.
# Una lista anidada se puede acceder utilizando varios índices.
# Una lista anidada se puede modificar utilizando varios índices.
# Una lista anidada se puede eliminar utilizando varios índices.
# Una lista anidada se puede añadir utilizando varios índices.

# Ejemplo
print("*********************** EJEMPLO 12+1: anidadas [matrices] **********************************")
print()

lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Lista anidada:", lista)
print("Primer elemento de la lista anidada:", lista[0])
print("Segundo elemento de la lista anidada:", lista[1])
print("Tercer elemento de la lista anidada:", lista[2])
print("Primer elemento de la primera lista:", lista[0][0])
print("Segundo elemento de la primera lista:", lista[0][1])
print("Tercer elemento de la primera lista:", lista[0][2])
print("Primer elemento de la segunda lista:", lista[1][0])
print("Segundo elemento de la segunda lista:", lista[1][1])
print("Tercer elemento de la segunda lista:", lista[1][2])
print("Primer elemento de la tercera lista:", lista[2][0])
print("Segundo elemento de la tercera lista:", lista[2][1])
print("Tercer elemento de la tercera lista:", lista[2][2])

# Recorrer los elementos de una lista anidada

# Los elementos de una lista anidada se pueden recorrer utilizando varios bucles for.
# Los elementos de una lista anidada se pueden recorrer utilizando varios bucles while.
# Los elementos de una lista anidada se pueden recorrer utilizando varios índices.
# Los elementos de una lista anidada se pueden recorrer utilizando varios rangos de índices.
# Los elementos de una lista anidada se pueden recorrer utilizando varios índices negativos.
# Los elementos de una lista anidada se pueden recorrer utilizando varios índices variables.

# Ejemplo
print("*********************** EJEMPLO 14: Recorrer anidadas [matrices] con bucles**********************************")
print()
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Recorrido con varios bucles for:")
for sublista in lista:
    for elemento in sublista:
        print(elemento)

print("Recorrido con varios bucles while:")
i = 0
while i < len(lista):
    j = 0
    while j < len(lista[i]):
        print(lista[i][j])
        j += 1
    i += 1  

print("Recorrido con varios índices:")
for i in range(len(lista)):
    for j in range(len(lista[i])):
        print(lista[i][j])

print("Recorrido con varios rangos de índices:")
for i in range(3):
    for j in range(3):
        print(lista[i][j])

print("Recorrido con varios índices negativos:")
for i in range(-3, 0):
    for j in range(-3, 0):
        print(lista[i][j])

print("Recorrido con varios índices variables:")
for i in [0, 2]:
    for j in [0, 2]:
        print(lista[i][j])
        
#Este ultimo ejemplo recorre 2 sublistas de la lista anidada y 2 elementos de cada sublista.  (posicion 0 y 2)

# En posicion 0,0 = 1
# En posicion 0,2 = 3
# En posicion 2,0 = 7
# En posicion 2,2 = 9
