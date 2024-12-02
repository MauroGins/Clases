"""Implementar un programa que verifique si un texto es "Twiteable" (tiene 280 caracteres o menos) o no.
El programa debe pedir un texto por teclado y mostrar un mensaje indicando si el texto es Twiteable o no."""




texto = input("Ingrese un texto: ")
if len(texto) <= 280:
    print("El texto es Twiteable")
else:
    print("El texto no es Twiteable")
        