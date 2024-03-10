import os
import sys

# Añadir el directorio principal al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Crear la ruta
def create_route(*args) -> str:

    # Unir los argumentos
    route = "/".join(args)

    # Retornar la ruta
    return os.path.abspath(route)

# Crear el directorio
def create_directory(route: str) -> None:
    if not os.path.exists(route):
        os.makedirs(route)