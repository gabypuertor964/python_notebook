import os
import sys

# Añadir el directorio principal al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Limpiar la consola
def clean() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
