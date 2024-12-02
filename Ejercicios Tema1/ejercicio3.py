# Ejercicio3
# Diseñar un algoritmo que pida una nota
# (valor entero) por teclado y dependiendo de su valor visualice la nota en letras.
# Por ejemplo, si nota es igual a 7 tiene que mostrar el texto "Notable".

# Forma bulgar con todo if
nota = int(input("ingrese una nota:"))

if nota < 5 and nota >= 0:
    print("Insuficiente")
if nota == 5:
    print("Suficiente")
if nota == 6:
    print("Bien")
if nota == 7 or nota == 8:
    print("Notable")
if nota == 9 or nota == 10:
    print("Sobresaliente")
if nota > 10 or nota < 0:
    print("Nota no válida")


# Otra forma

if nota < 5 and nota >= 0:
    print("Insuficiente")
elif nota == 5:
    print("Suficiente")
elif nota == 6:
    print("Bien")
elif nota == 7 or nota == 8:
    print("Notable")
elif nota == 9 or nota == 10:
    print("Sobresaliente")
else:
    print("Nota no válida")

# Para un ingreso de nota de 0-100 y se divide entre el entero. 55 -> 5 100 -> 10

nota = nota // 10

match nota:
    case 0 | 1 | 2 | 3 | 4:
        print("Insuficiente")
    case 5:
        print("Suficiente")
    case 6:
        print("Bien")
    case 7 | 8:
        print("Notable")
    case 9 | 10:
        print("Sobresaliente")
    case _:
        print("Nota incorrecta ")
