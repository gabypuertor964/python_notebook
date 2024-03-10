"""
    Registrar la ruta del proyecto en el path de python
"""
def root_directory():

    # Importar los modulos requeridos
    import os
    import sys

    # Obtener la ruta del proyecto
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Agregar la ruta del proyecto al path de python
    sys.path.append(project_path)
root_directory()

from tools.old.display import *
from tools.old.inputs import *

dictionary = {}

while True:
    title("Traductor de Frutas",True)

    subtitle(f"Actualmente contamos con {len(dictionary)} traducciones")

    # Obtener el nombre de la fruta a traducir
    fruit = clean_spaces(get("Ingrese una fruta (q para salir): ")).lower()

    if(fruit == "q"):
        break

    if fruit in dictionary:
        subtitle(f"La traduccion de {fruit} es {dictionary[fruit]}")
        input_skip()
    else:   
        while True:
            title("Traductor de Frutas",True)

            option = get("La fruta no se encuentra en el diccionario, ¿Desea agregarla? (1. Si - 2. No): ")

            if(is_number(option) and int(option) in range(1,3)):

                # Opcion: Si
                if(int(option) == 1):
                    space()

                    dictionary[fruit] = clean_spaces(get("Ingrese la traduccion de la fruta: ")).lower()
                    
                    subtitle("Traduccion agregada con exito")
                    input_skip()
                    break

                # Opcion: No / Salir
                if(int(option) == 2):
                    break
