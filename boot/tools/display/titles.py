import os.path as path 
import sys

# Añadir el directorio principal al path
sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

from tools.console.clean import clean
from tools.display.text_align import center
from tools.input.clean import trim_spaces


# Imprimir el titulo principal del programa
def title(text: str, is_clean: bool = True, have_space: bool = True) -> None:

    # Limpiar la consola si es necesario
    if is_clean:
        clean()

    # Retornar el titulo principal
    print(f"{center(text)}")

    # Agregar un espacio si es necesario
    if have_space:
        print()


# Imprimir el mensaje de error
def error(text: str) -> None:

    # Limpiar la cadena
    text = trim_spaces(text)

    # Retornar el mensaje de error
    print(f"{center(text, '!')}")


# Imprimir el mensaje de cierra del programa
def bye(text: str = "Gracias por usar el notebook de Gaby Puerto", does_clean: bool = True) -> None:

    # Limpiar la consola si es necesario
    if does_clean:
        clean() 

    # Notificacion de salida
    print("Finalizando ejecucion...")

    # Retornar el mensaje de despedida
    print(f"{center(text, "*")}")
