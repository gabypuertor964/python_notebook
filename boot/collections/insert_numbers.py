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

numbers = []

def insert_numbers(num_numbers: int):

    for x in range(1,num_numbers+1):

        while True:

            title("Insertar numeros",True)

            option = get(f"Ingrese el numero ({x}): ")

            if(is_number(option)):
                numbers.append(option)
                subtitle("Numero ingresado correctamente")
                input_skip()
                break
            else:
                subtitle("El valor ingresado no es un numero")
                input_skip()

def show_numbers():
    global numbers

    title("Numeros Ingresados",True)
    
    for number in numbers:

        subtitle(number)

while True:
    title("Insertar numeros",True)
    option = get("Ingrese el numero de numeros a insertar: ")

    if(is_number(option) and int(option) > 0):
        insert_numbers(int(option))

    show_numbers()
    input_skip()
    break;
