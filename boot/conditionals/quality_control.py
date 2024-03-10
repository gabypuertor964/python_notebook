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

"""
    Tinder: Crear un buscador de parejas permitiendo ingresar las siguientes opciones:

    * Soltera, linda de 20 años, mala persona
    * Soltera, fea de 45 años, buena persona
    * Soltera, linda de 31 años, mala persona
    * Casada, linda de 25 años, buena persona
"""
from tools.old.display import *
from tools.old.inputs import *

def verify(option: int):

    title("Control de Calidad",True)

    if(option == 1):
        subtitle("El producto cumple con los requisitos de calidad")
    elif(option == 2):
        subtitle("El producto ha salido defectuoso, se detiene la produccion")

while True:

    title("Control de Calidad",True)

    options = [
        'Si',
        'No'
    ]
    print_options(options,"¿El producto cumple con el estandar de calidad?")

    option = get()

    if(is_number(option) and int(option) in range(1,4)):

        # Verificar si la opcion es regresar
        if(int(option) == 3):
            break

        verify(int(option))
        input_skip()