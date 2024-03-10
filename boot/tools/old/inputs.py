"""
    Limpiar y formatear los inputs de texto
"""

# Obtener un input de texto
def get(message: str = "Ingrese una opcion: ") -> None:
    text = input(f"\t{message}".expandtabs(8))
    return clean_spaces(text)

# Eliminar los espacios innecesarios de una cadena de texto
def clean_spaces(text) -> str:

    # Eliminar espacios al inicio y al final
    text = text.strip()

    # Obtener el listado de palabras
    words = text.split()

    # Crear una nueva cadena de texto con las palabras
    text = " ".join(words)

    # Retornar el texto
    return text

# Verificar si el input es un numero
def is_number(input) -> bool:
    try:
        float(input)
        return True
    except:
        return False

# Ralizar la verificacion numerica a una lista de inputs   
def is_number_list(list: list) -> bool:
    for item in list:
        if not is_number(item):
            return False
    return True

def input_skip():
    get("Presione cualquier tecla para regresar ")