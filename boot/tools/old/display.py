from shutil import get_terminal_size
from .inputs import clean_spaces
import os

"""
    Modulo para mostrar contenido formateado y estilizado en la consola
"""

def clean_console() -> None:
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def space() -> None:
    print()

def text_center(text: str, character: str = " ") -> None:

    # Eliminar los caracteres innecesarios de la cadena
    text = clean_spaces(text)

    # Obtener el ancho de la terminal
    weight = get_terminal_size().columns

    # Obtener el espacio a cada lado del texto
    space = (weight - len(text) - 2) // 2

    # Crear la linea de caracteres
    line = character * space + " " + text + " " + character * space

    # Imprimir la linea
    print(line)

def title(text: str, clean: bool = False) -> None:

    # Limpiar la consola si es necesario
    if(clean):
        clean_console()
    
    space()
    text_center(text, "=")
    space()

def indentation(text: str, title: bool = False) -> str:

    # Adicionar los dos puntos si es necesario
    if(not title):
        return f"\t{text}: ".expandtabs(8)
    else:
        return f"\t{text}".expandtabs(8)

def print_options(options, message: str = "Ingrese una opcion", back_message: str = "Regresar", back: bool = True) -> None:

    if (isinstance(options, list)):
        # Añadir el primer elemento del menu 
        menu = indentation(message) + f" 1. {options[0]} \n"

        # Añadir los elementos restantes del menu alineados con el primero
        for i in range(1, len(options)):
            menu += " " * (len(indentation(message))+1) + f"{i+1}. {options[i]} \n"
    else:
        first = True
        for i, key in enumerate(options, start=1):
            if first:
                menu = indentation(message) + f" {i}. {key} \n"
                first = False
            else:
                menu += " " * (len(indentation(message)) + 1) + f"{i}. {key}\n"

    # Verificar si se debe agregar la opcion de regresar
    if(back):
        menu += "\n" + " " * (len(indentation(message))+1) + f"{len(options)+1}. {back_message} \n"

    print(menu)

def subtitle(text: str) -> None:
    print(indentation(text,True))
    print()

def close() -> None:
    clean_console()
    
    space()
    print("Finalizando ejecucion...")
    text_center("Gracias por usar el notebook de Gaby Puerto","=")
    space()