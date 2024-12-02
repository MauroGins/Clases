"""
Implementar un programa de registro y login de usuarios. En primer lugar se ejecutará el código de registro,
que solicitará un nombre de usuario y una contraseña. A continuación, se ejecutará el código de login, que 
solicitará el nombre de usuario y la contraseña. Si el nombre de usuario y la contraseña coinciden con los 
introducidos en el registro, se mostrará un mensaje de bienvenida. En caso contrario, se mostrará un mensaje 
de error. Necesitaremos una función para el registro y otra para el login. Y las llamadas a las funciones de
registro y login se realizarán en el algoritmo principal.
"""


def register():
   
    print("*********Registrese aquí:*********")
    name_user = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    return name_user, password
# end def

def login():
  
    print("*********Logeate aquí:*********")
    name_user = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    return name_user, password
# end def

def main():
    
    print("Bienvenido a nuestro sistema de registro y login de usuarios")
    name_user, password = register()
    name_user2, password2 = login()
    if name_user == name_user2 and password == password2:
        print("Bienvenido")
    else:
        print("Error")
    # end def
    
    
    
if __name__ == "__main__":
    main()
    # end if
    