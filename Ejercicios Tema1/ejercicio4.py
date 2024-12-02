# Diseñar un algoritmo que lea 20 caracteres de teclado y muestre por pantalla el número de veces que se repiten cada una de las vocales.


a = 0
e = 0
i = 0
o = 0
u = 0

for x in range(20):

    char = ""
    while (
        len(char) != 1
    ):  # aqui le decimos que el cuente el caracter distinto a 1 y si hay mas de 1 caracter no lo cuenta y se repite el mensaje
        char = input("Introduzca un mensaje de 20 caracteres: " + str(x + 1) + "/20 \n")
        if (
            len(char) != 1
        ):  # aqui te dice que has metido dos caracteres y no uno, y debes ingresar TAN SOLO UNO
            print("Debe ingresar solo UN caracter")
    match char.lower():
        case "a":
            a += 1
        case "e":
            e += 1
        case "i":
            i += 1
        case "o":
            o += 1
        case "u":
            u += 1

print("La boca <a> se repite", a, "veces")
print("La boca <e> se repite", e, "veces")
print("La boca <i> se repite", i, "veces")
print("La boca <o> se repite", o, "veces")
print("La boca <u> se repite", u, "veces")



#OTRA OPCION con cadena larga de strings para contar vocales en palabra

print("ingrese 20 caracteres")
caracteres = input().lower()
vueltas = 0
if len(caracteres) > 20:
    vueltas = 20
else:
    vueltas = len(caracteres)


for x in range(vueltas):
    match caracteres[x]:
        case "a":
            a += 1
        case "e":
            e += 1
        case "i":
            i += 1
        case "o":
            o += 1
        case "u":
            u += 1

print("La boca <a> se repite", a, "veces")
print("La boca <e> se repite", e, "veces")
print("La boca <i> se repite", i, "veces")
print("La boca <o> se repite", o, "veces")
print("La boca <u> se repite", u, "veces")