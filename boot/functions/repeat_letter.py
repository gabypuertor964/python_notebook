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

# Constructor de diccionario
def repeat_letter(word):

    # Limpiar palabra
    word = word.replace(" ","").lower()

    # Crear conjunto de letras
    letters = set(word)

    # Crear diccionario de letras
    letters_dict = {}

    for letter in letters:
        letters_dict[letter] = word.count(letter)

    return letters_dict

while True:

    # Titulo principal
    title("Buscar letras repetidas",True)

    value = get("Ingrese una palabra (-1 para salir): ").lower()

    # Verificar si se indico salir
    if(value == "-1"):
        break

    # Verificar que el valor ingresado sea una palabra
    if(is_number(value)):
        subtitle("El valor ingresado no es una palabra")
        input_skip()
    else:
        # Ejecutar conteo y visualizar resultado
        subtitle(f"En la palabra {value} sus letras se repiten: {repeat_letter(value)}")
        input_skip()