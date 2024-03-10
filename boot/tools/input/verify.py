import os.path as path 
import sys

# Añadir el directorio principal al path
sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

# Verificar que todos los elementos de una lista sean numeros
def is_numbers(values: list) -> bool:

    for value in values:
        if not value.isdigit():
            return False

    return True

# Verificar que todos los numeros sean positivos
def is_positive(values: list) -> bool:

    for value in values:
        if not float(value) > 0:
            return False

    return True