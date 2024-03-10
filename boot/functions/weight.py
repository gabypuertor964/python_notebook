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

weight_1 = 147
weight_2 = 2400

units_1 = 0
units_2 = 0

# Calcular el peso
def generate_weight():
    
    # Titulo principal
    title("Resultado",True)

    # Mostrar los resultados
    subtitle(f"El peso total es: {try_int((weight_1 * units_1) + (weight_2 * units_2))} unidades de peso")

    input_skip()

while True:

    while True:

        # Titulo principal
        title("Paquete tipo 1",True)

        # Solicitar el valor
        value = get("Cantidad de paquetes comprados (q para salir): ")

        # Verificar si se desea salir
        if value.lower() == "q":
            break

        # Verificar si el valor es numerico
        if (value.isdigit() and int(value) > 0):
            units_1 = int(value)
            break

    while True:

        # Titulo principal
        title("Paquete tipo 2",True)

        # Solicitar el valor
        value = get("Cantidad de paquetes comprados (q para salir): ")

        # Verificar si se desea salir
        if value.lower() == "q":
            break

        # Verificar si el valor es numerico
        if (value.isdigit() and int(value) > 0):
            units_2 = int(value)
            break

    generate_weight()
