import os.path as path 
import sys

# Añadir el directorio principal al path
sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

from tools.display.text_align import left


# Imprimir las opciones del menu segun una lista o diccionario
def print_menu(options: list | dict, select_message: str = "Seleccione una opcion", back_necesary: bool = True, back_message: str = "Regresar") -> None:

    # Inicializar el menu
    menu = ""

    # Escenario 1: Si las opciones son una lista
    if isinstance(options, list):

        # Generar la primera linea
        first_line = left(select_message)

        # Concatenar la primera opcion del menu
        if isinstance(options[0], str):  

            # Escenario: Si las opciones son una lista de strings
            menu = first_line + f"1. {options[0]} \n"
        else:
            # Escenario: Si las opciones son una lista de listas (Nombre, funcion)
            menu = first_line + f"1. {options[0][0]} \n"

        # Concatenar las demas opciones en el menu respetando la sangria respecto a la primera opcion
        for index, option in enumerate(options[1:], 2):
            
            if isinstance(option, str):
                menu += (" " * (len(first_line))) + f"{index}. {option} \n"
            else:
                menu += (" " * (len(first_line))) + f"{index}. {option[0]} \n"

    # Escenario 2: Si las opciones son un diccionario
    else:

        # Variable de control para la primera opcion
        first = True

        for number, key in enumerate(options, 1):

            if first:
                menu = left(select_message) + f" {number}. {key} \n"
                first = False
            else:
                menu += " " * (len(left(select_message)) + 1) + f"{number}. {key}\n"

    # Escenario 3: Si se necesita la opcion de regresar
    if back_necesary:
        menu += "\n" + " " * (len(left(select_message))) + f"{len(options) + 1}. {back_message} \n"

    print(menu)
