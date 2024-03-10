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

title("Deletreador de palabra",True)

option = str(get("Ingrese la palabra a deletrear: ")).lower()
conjunto = set(option)

subtitle(f"Las letras de la palabra ingresada son: {conjunto}")
input_skip()