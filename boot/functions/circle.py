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
from math import pi

# Generar el valor del area
def generate_area(radius:float):

    # Titulo principal
    title("Resultado",True)

    # Mostrar los resultados
    subtitle(f"Radio: {try_int(radius)}")
    subtitle(f"Area: {try_int(pi * (radius ** 2))}")

    input_skip()

while True:

    # Titulo principal
    title("Calcular area de un circulo",True)

    # Solicitar el valor
    value = get("Ingrese el valor del radio (q para salir): ")

    # Verificar si se desea salir
    if value.lower() == "q":
        break

    # Verificar si el valor es numerico
    if (value.isdigit() and float(value) > 0):
        # Generar el area
        generate_area(float(value))
