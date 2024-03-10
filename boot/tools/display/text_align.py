import os.path as path 
import sys

# Añadir el directorio principal al path
sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

from tools.input.clean import trim_spaces
from tools.console.get_size import get_size


# Posicionar el texto a la izquierda
def left(text: str, is_list: bool = True) -> str:

    # Limpiar los espacios inecesarios
    text = trim_spaces(text)

    # Concatenar el texto en caso de ser una lista
    text = text + ": " if is_list else text + " "

    # Retornar el texto a la izquierda
    return f"{" " * 8 + text}"


# Posicionar el texto a la derecha
def right(text: str, is_list: bool = True) -> str:

    # Limpiar los espacios inecesarios
    text = trim_spaces(text)

    # Concatenar el texto en caso de ser una lista
    text = " :" + text if is_list else " " + text

    # Obtener el ancho de la consola
    width = get_size()["width"]

    # Calcular la cantidad de espacios en blanco al principio
    spaces = width - len(text) - 10

    # Retornar el texto a la derecha con la misma sangría
    return f"{' ' * spaces} {text} {' ' * 8}"


# Centrar el texto en la consola
def center(text: str, character: str = "=") -> str:

    # Limpiar los espacios inecesarios
    text = trim_spaces(text)

    # Obtener el ancho de la consola
    width = get_size()["width"]

    # Calcular los espacios x lado
    spaces = (width - len(text) - 2) // 2

    # Retornar el texto centrado
    return f'{character * spaces} {text} {character * spaces}'
