"""
    Registrar la ruta del proyecto en el path de python
"""
def root_directory():

    # Importar los modulos requeridos
    import os
    import sys

    # Obtener la ruta del proyecto
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Agregar la ruta del proyecto al path de python
    sys.path.append(project_path)
root_directory()

from tools.old.display import *
from tools.old.inputs import *

password = "123456789"
tries = 0

def password_verify(password_input: str):
    global tries
    title('Password Verify',True)

    if(password_input == password):
        subtitle("La contraseña ingresada es correcta")
    else:
        tries += 1

        if(tries >= 5):
            subtitle("Ha superado el numero de intentos")
            return False
        else:
            subtitle("La contraseña ingresada es incorrecta")

    return True

while True:

    title("Password Verify", True)

    # Obtener el password
    password_input = get(f"Ingrese el contraseña te quedan {5 - tries} intentos (q para salir) : ")

    # Validar si se ingreso la opcion de salir
    if(password_input == "q"):
        break

    # Validar la contraseña
    response = password_verify(password_input)
    input_skip()

    if(not response):
        break