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
from tools.old.transform import *

even = set()
odd = set()

def clasificator():

    while True:
        title("Clasificador de numeros",True)

        option = get("Ingrese un numero (q para salir): ")

        # Validar si es un numero
        if(is_number(option)):

            # Convertir a entero (si es posible)
            number = try_int(option)

            # Clasificar
            if(number % 2 == 0):
                even.add(number)
            else:
                odd.add(number)

        elif(option.lower() == "q"):
            break
        else:
            subtitle("El valor ingresado no es un numero")
            input_skip()

while True:

    # Titulo principal
    title("Clasificador de numeros",True)

    options = [
        "Ingresar un numero",
        "Ver numeros pares",
        "Ver numeros impares"
    ]
    print_options(options)

    option = get()

    # Validar que la opcion sea valida
    if(is_number(option) and int(option) in range(1,len(options)+2)):

        # Opcion: Salir
        if(int(option) == len(options)+1):
            break

        # Opcion: Ingresar un numero
        if(int(option) == 1):
            clasificator()

        # Opcion: Ver numeros pares
        if(int(option) == 2):

            title("Clasificador de numeros",True)

            if(len(even) == 0):
                subtitle("No hay numeros pares registrados")
                input_skip()
            else:    
                subtitle(f"Numeros pares {sorted(even)}")
                input_skip()

        # Opcion: Ver numeros impares
        if(int(option) == 3):

            title("Clasificador de numeros",True)

            if(len(odd) == 0):
                subtitle("No hay numeros impares registrados")
                input_skip()
            else:
                subtitle(f"Numeros impares {sorted(odd)}")
                input_skip()