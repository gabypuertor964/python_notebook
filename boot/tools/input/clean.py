import os.path as path 
import sys
import re

# Añadir el directorio principal al path
sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

# Eliminar los espacios inecesarios de una cadena
def trim_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())
