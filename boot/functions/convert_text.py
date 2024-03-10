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
from tools.old.transform import *

text_numbers = {
    "0": "cero",
    "1": "uno",
    "2": "dos",
    "3": "tres",
    "4": "cuatro",
    "5": "cinco",
    "6": "seis",
    "7": "siete",
    "8": "ocho",
    "9": "nueve",
}

def convert_text(number):

    digits = list(str(number))
    text = ""

    for digit in digits:
        text += f"{text_numbers[digit]} - "

    # Remover el último guión y espacio
    text = text[:-3]

    # Retornar el texto
    return text

while True:

    title("Convertir numero a texto",True)

    value = get("Ingrese un numero (q para salir): ")

    # Verificar si se indico salir
    if(value.lower() == "q"):
        break

    # Verificar si el valor ingresado es un numero
    if(value.isdigit()):

        title("Convertir numero a texto",True)

        subtitle(f"El numero {value} en texto es: {convert_text(int(value))}")
        input_skip()
    else:
        subtitle("El valor ingresado no es un numero")
        input_skip()