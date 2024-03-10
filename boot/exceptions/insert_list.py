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

"""
    Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar
"""

from tools.old.display import *
from tools.old.inputs import *

# Lista vacia de elementos
items = list()

# Funcion para agregar un elemento a la lista
def insert_list(value) -> dict:
    
    data = {}

    try:
        # Verificar si el elemento ya existe
        if value in items:
            raise ValueError('El elemento ya existe en la lista')

        # Agregar el elemento a la lista
        items.append(value)

        # Estado de la operacion
        data['status'] = True

        # Mensaje de operacion
        data['value'] = f'El elemento {value} fue añadido a la lista'

    except ValueError as error:

        # Estado de la operacion
        data['status'] = False

        # Mensaje de error
        data['value'] = error

    finally:

        # Mensaje de salida
        data["finally_message"] = "Gracias por usar este programa"

    return data

while True:

    # Titulo principal
    title('Insertar un elemento en una lista',True)

    # Listado e impresion de opciones
    options = [
        'Agregar un elemento a la lista',
        'Mostrar la lista',
    ]
    print_options(options)

    # Obtener la opcion seleccionada
    option = get()

    if(option.isdigit() and int(option) in range(1, len(options)+2)):
        
        # Validar si se selecciono la opcion de salir
        if(int(option) == len(options)+1):
            break

        # Validar si se selecciono la opcion de agregar un elemento
        if(int(option) == 1):

            # Titulo principal
            title('Insertar elemento',True)

            # Solicitar el valor a ingresar
            value = get("Ingrese el valor a añadir: ")

            # Agregar el valor a la lista y almacenar el resultado de la operacion
            data = insert_list(value)

            # Imprimir datos de operacion
            subtitle(data["value"])

            # Imprimir mensaje de salida
            subtitle(data["finally_message"])

            # Pausa para leer los mensajes
            input_skip()
        
        # Validar si se selecciono la opcion de mostrar la lista
        if(int(option) == 2):

            # Titulo principal
            title('Lista de elementos',True)

            # Imprimir la lista
            subtitle(f'Lista de elementos: {items}')

            # Pausa para leer los mensajes
            input_skip()