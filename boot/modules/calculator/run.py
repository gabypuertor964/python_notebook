import os
import sys

# Añadir el directorio principal al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from tools.display.titles import title, error
from tools.display.text_align import left
from tools.display.menu import print_menu
from tools.input.get import get, wait
from tools.input.transform import float_or_int

from operations import directory,run

def get_args():

    # Indice de ejecucion
    index = 1

    # Listado de parametros
    args = []

    while True:

        # Titulo principal
        title("Ingreso de parametros")

        # Obtener el parametro
        param = get(f"Parametro {index} (q para salir)")

        # Verificar si el parametro es q
        if param.lower() == "q":

            if len(args) < 2:
                wait("Debes ingresar al menos 2 parametros")
            else:
                return args

        # Verificar si el parametro es un numero
        if param.isdigit():
        
            # Añadir el parametro a la lista y aumentar el indice
            args.append(float_or_int(float(param)))
            index += 1

        elif param.lower == "q":
            # Control: Para salir deben haber al menos 2 parametros
            if len(args) < 2:
                wait("Debes ingresar al menos 2 parametros")
            else:
                return args  
        else:
            wait("Debes ingresar un numero")

while True:
    
    # Titulo principal
    title("Calculadora")

    # Imprimir el menu
    print_menu(directory)

    # Obtener la operacion
    operation = get("Seleccione la operacion")

    if operation.isdigit() and int(operation) in range(1, len(directory) + 2):
        
        # Opcion: Salir
        if int(operation) == len(directory) + 1:
            break

        # Obtener los argumentos
        args = get_args()

        # Ejecutar la operacion
        result = run(args, int(operation))

        if result["status"]:
            title(f"Operacion: {result['operation']}")
            print(left("Resultado: " + str(result["result"]),False))
        else:
            title("Error")
            error(result["message"])
        wait()
    