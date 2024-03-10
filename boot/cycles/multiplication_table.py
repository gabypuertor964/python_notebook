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

number = 0
limit = 0

def multiplication(number: int):

    title("Tabla de multiplicar", True)

    for i in range(1, 11):
        subtitle(f"{number} x {i} = {number*i}")

while True:
    
    title("Tabla de multiplicar", True)
        
    # Obtener el numero a multiplicar
    number = get("Ingrese el numero a multiplicar (q para salir): ")

    # Verificar si el input es un numero
    if(is_number(number)):
        number = multiplication(int(number))
        input_skip()

        break
    elif(number == "q"):
        break
