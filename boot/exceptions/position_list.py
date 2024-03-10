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
    Finaliza el siguiente código con una gestión completa de sus excepciones. El objetivo del programa es solicitar al usuario una posición de una lista y devolver el valor que se encuentra en dicha posición. Prueba el programa enviando una posición inexistente y enviando una letra como posición. El programa sólo terminará cuando se ejecute correctamente
"""

from tools.old.display import *
from tools.old.inputs import *

# Lista de numeros registrados
numbers = [3,5,6,8]

# Funcion para obtener un numero de la lista
def get_number(position:str) -> dict:
    
    # Diccionario de datos de salida
    data = {}

    try:
        # Estado de la operacion
        data['status'] = True

        # Obtener el valor de la posicion
        data['value'] = numbers[int(position)]

    # Excepcion: Valor no numerico
    except ValueError:

        # Estado de la operacion
        data['status'] = False

        data['value'] = 'La posicion ingresada no es un numero'

    # Excepcion: Posicion no existente
    except IndexError:
        # Estado de la operacion
        data['status'] = False

        data['value'] = 'La posicion ingresada no existe en la lista'

    # Excepcion: Error desconocido
    except:
        # Estado de la operacion
        data['status'] = False

        data['value'] = 'Error desconocido'

    return data

while True:

    # Titulo principal
    title('Lista de numeros',True)

    # Obtener el valor de la posicion a consultar
    position = get('Ingrese la posicion del numero a consultar: ')

    # Ejecutar la funcion para obtener el valor de la posicion y almacenar los datos de retorno
    data = get_number(position)

    # Escenario: Exito
    if(data['status']):
        subtitle(f'El valor en la posicion {position} es {data["value"]}')
        input_skip()
        break

    # Escenario: Error
    else:
        subtitle(data['value'])
        input_skip()