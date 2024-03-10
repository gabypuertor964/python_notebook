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

title("Tuplas",True)

# Solicitar la frase
value = get("Ingrese una frase: ")

# Limpiar la frase
value = value.lower().replace(" ","")

# Crear la tupla
lista = [value]
tupla = tuple(lista)

# Mostrar la tupla
subtitle(f"Tupla: {tupla}")

input_skip()