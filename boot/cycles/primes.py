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

numbers = []

def is_prime(number):
    if number < 2:
        return False
    
    for n in range(2, int(number**0.5) + 1):
        if number % n == 0:
            return False
    return True

for number in range(1, 10001):
    if is_prime(number):
        numbers.append(str(number))  # Convierte el número a cadena

title("Primos", True)
subtitle("Los numeros primos del 1 al 10000 son: ") 

for number in numbers:
    subtitle(f"* {number}")
input_skip()