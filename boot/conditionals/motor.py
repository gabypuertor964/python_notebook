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

def status(temp: float):

    title("Motor manager",True)

    if(temp > 80):
        subtitle("El motor esta sobrecalentado, por lo cual se apagara")
    else:
        subtitle("El motor tiene buena temperatura, esta encendido")

while True:

    title("Motor manager",True)
    option = get("Ingrese la temperatura actual del motor (-1 para salir): ")
    
    # Verificar si el input es un numero
    if(is_number(option)):

        if(int(option) == -1):
            break   
        
        status(float(option))
        input_skip()
        break