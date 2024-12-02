secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
while True:
    num = int(input("¿Sabes ya que número es? "))
    if num == secret_number:
        print("¡Bien hecho, muggle! Eres libre ahora")
        break
    else:
            print("¡Ja, ja, ja! ¡Estás atrapado en mi bucle!")
