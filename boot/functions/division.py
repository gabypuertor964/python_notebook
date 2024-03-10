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

number_n = 0
number_m = 0

def division():

    # Titulo principal
    title("Resultado",True)

    # Generar y mostrar los resultados
    results = [
        f"Numero n: {number_n}",
        f"Numero m: {number_m}",
        f"Cociente: {number_n // number_m}",
        f"Residuo: {number_n % number_m}",
    ]
    print_options(results,"Informacion","",False)
    input_skip()

while True:

    # Titulo principal
    title("Division de dos numeros",True)

    while True:

        # Titulo principal
        title("Valor primer numero",True)

        # Solicitar el valor
        number_n = get("Ingrese el valor (q para salir): ")

        # Verificar si se desea salir
        if(number_n.lower() == "q"):
            break

        if(number_n.isdigit() and int(number_n) > 0):
            
            # Almacenar el valor y salir
            number_n = int(number_n)
            break

    while True:
            
        title("Valor segundo numero",True)

        # Solicitar el valor
        number_m = get("Ingrese el valor (q para salir): ")
    
        # Verificar si se desea salir
        if(number_m.lower() == "q"):
            break
    
        if(number_m.isdigit() and int(number_m) > 0):
                
            # Almacenar el valor y salir
            number_m = int(number_m)
            break

    division()
