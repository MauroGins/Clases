# Ejercicio 2

# Escribir una función que reciba un diccionario con el horario de un alumno y lo recorra imprimiendo los días de la semana y las asignaturas que tiene en cada uno.

def imprimir_horario(diccionario: dict) -> None:
    try:
        for dia, asignaturas in diccionario.items():
            print(f"{dia}: {', '.join(asignaturas)}")
    except AttributeError:
        print("Por favor, introduzca un diccionario con los días de la semana y las asignaturas correspondientes")
    except TypeError:
        print("Por favor, introduzca un diccionario con los días de la semana y las asignaturas correspondientes")
    except:
        print("Ha ocurrido un error")

# Pruebas
imprimir_horario({"Lunes": ["Matemáticas", "Lengua"], "Martes": ["Historia", "Inglés"], "Miércoles": ["Física", "Química"]})    
# Lunes: Matemáticas, Lengua
# Martes: Historia, Inglés
# Miércoles: Física, Química
