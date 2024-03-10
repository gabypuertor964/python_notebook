import os.path as path 
import sys

# Añadir el directorio principal al path
sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

from tools.input.clean import trim_spaces
from tools.display.text_align import left


# Solciitar al usuario que ingrese un valor
def get(text: str = "Ingrese una opcion") -> str:

    # Limpiar cadena
    text = trim_spaces(text)

    # Solicitar al usuario que ingrese un valor
    return trim_spaces(input(f"{left(text)}"))


# Input de espera
def wait(text: str = "Presione enter para continuar") -> None:

    # Limpiar cadena
    text = trim_spaces(text)

    print()
    # Solicitar al usuario que presione enter
    input(f"{left(text, False)}")
