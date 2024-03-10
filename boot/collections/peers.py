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

list_a = ["ma", "me", "mi", "mo", "mu"]
list_b = ["pa", "pe", "pi", "po", "pu"]

title("Listas",True)

for index in range(len(list_a)):
    subtitle(list_a[index] + " - " + list_b[index])

input_skip()