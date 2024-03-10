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

numbers = set()

def even_recursive(number: int):

    global numbers

    # Verificar si el numero es 1 (Limite inferior)
    if(number == 1):
        return numbers

    # Verificar si el numero es par y agregarlo al conjunto
    if(number % 2 == 0):
        numbers.add(number)
    
    return even_recursive(number-1)

while True:

    title("Generador de numeros pares",True)

    value = get("Ingrese el limite superior del rango (q para salir): ")

    # Verificar si se indicio salir
    if(value.lower() == "q"):
        break

    # Verificar si el valor ingresado es un numero
    if(is_number(value)):

        title("Generador de numeros pares",True)

        subtitle(f"Los numeros pares generados son: {even_recursive(try_int(value))}")
        input_skip()
    else:
        subtitle("El valor ingresado no es un numero")
        input_skip()