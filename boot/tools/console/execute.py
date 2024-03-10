import os.path as path 
import sys

# Añadir el directorio principal al path
sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

# Forzar una excepcion
def force_exception(exception, message: str = None):
    if message == None:
        raise exception
    else:
        raise exception(message)

# Ejecutar una funcion y manejar las excepciones
def execute(function, custom_message: bool = False):
    try:
        return {"status": True,"result": function()}
    except (TypeError, ZeroDivisionError, IndexError, StopIteration) as exception:

        if not custom_message:
            # Mensajes por default
            if type(exception) == TypeError:
                message = "Argumentos invalidos"
            elif type(exception) == ZeroDivisionError:
                message = "No puedes dividir entre 0"
            elif type(exception) == IndexError:
                message = "Elemento fuera de rango"
            elif type(exception) == StopIteration:
                message = "Lista vacia"
        else:
            message = str(exception)

        return {"status": False, "message": message}
    except Exception as message:
        return {"status": False,"message": f"Excepcion General -> Detallado: {str(message)}"}