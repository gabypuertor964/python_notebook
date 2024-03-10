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
    Run: Menu dinamico de ejecucion de los scripts
"""
from tools.old.display import *
from tools.old.inputs import *

value = 0
discount_rate = 0
stratum = 0
age = 0
status = True

def discount():

    title("Descuendo de Matricula",True)

    if(stratum == 1 and age < 18):
        discount_rate = 20
    elif(stratum == 1 and age >= 18):
        discount_rate = 15
    elif(stratum == 2 and age < 18):
        discount_rate = 10
    elif(stratum == 2 and age >= 18):
        discount_rate = 5

    value_discount = value * (discount_rate/100)

    message = f"""
        * Valor neto: ${value}
        * Porcentaje de descuento: {discount_rate}%
        * Valor del descuento: ${value_discount}
        * Valor final: {value - value_discount}
    """
    print(message)

while status:

    # Obtener y almacenar el valor de la matricula
    while status:

        title("Descuendo de Matricula",True)
        option = get("Ingrese el valor de su matricula (-1 para salir): ")

        # Valir que el input sea un numero
        if(is_number(option)):

            # Verificar si se selecciono regresar
            if(int(option) == -1):
                status = False
                break

            if(int(option) > 0):
                value = int(option)
                break
                
    # Obtener y almacenar el estrato
    while status:

        title("Descuendo de Matricula",True)
        option = get("Ingrese su estrato (1,2): ")
    
        if(is_number(option) and int(option) in range(1,3)):

            stratum = int(option)
            break

    # Obtener y almacenar la edad
    while status:
        title("Descuendo de Matricula",True)
        option = get("Ingrese su edad: ")

        if(is_number(option) and int(option) in range(1,100)):
            age = int(option)

            discount()
            input_skip()
            break
    
    if(not status):
        break