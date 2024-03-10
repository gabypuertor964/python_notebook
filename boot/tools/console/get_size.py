import os.path as path 
import sys

# Añadir el directorio principal al path
sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

from shutil import get_terminal_size


# Obtener y retornar el tamaño de la consola
def get_size() -> dict:
    return {
        "width": get_terminal_size().columns,
        "height": get_terminal_size().lines
    }
