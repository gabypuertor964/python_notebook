import os
import sys

# Añadir el directorio principal al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from tools.console.execute import execute, force_exception

# Sumar n numeros
def sum_custom(numbers: list[int|float]):
    return execute(lambda: sum(numbers))

# Restar 2 numeros
def substract(numbers: list[int|float]):
    return execute(lambda: eval('-'.join(map(str, numbers))))

# Multiplicar n numeros
def multiply(numbers: list[int|float]):
    return execute(lambda: eval('*'.join(map(str, numbers))))

# Dividir 2 numeros
def divide(numbers: list[int|float]):
    return execute(lambda: eval('/'.join(map(str, numbers))))

# Directorio de operaciones
directory = [
    ["Suma", sum_custom],
    ["Resta", substract],
    ["Multiplicacion", multiply],
    ["Division", divide]
]

def run(args: list, operation: int|float):

    # Verificar el numero de argumentos y su tipo
    if len(args) < 2 or not all(isinstance(num, (int, float)) for num in args):
        return execute(lambda: force_exception(TypeError, "Argumentos insuficientes o invalidos"), True)
    
    try:
        # Obtener informacion de la operacion
        operation_name, operation = directory[operation - 1]

        # Ejecutar la operacion
        result = operation(args)

        # Añadir el nombre de la operacion al resultado
        result["operation"] = operation_name

        # Retornar el resultado
        return result
    except IndexError:
        return execute(lambda: force_exception(IndexError,"Operacion invalida"), True)
    except Exception:
        return execute(lambda: force_exception(Exception))