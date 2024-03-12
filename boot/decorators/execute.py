from sqlite3 import Error as SqliteError

# Ejecutar de forma segura las operaciones
def execute(*args, debug=False):

    # Funcion decorada
    def decorator(function):
        def run(*args, **kwargs):
            
            # Diccionario de respuestas
            responses = {
                TypeError: "Argumentos invalidos",
                ZeroDivisionError: "No se puede dividir entre 0"
            }

            try:
                return {"status": True,"result": function(*args, **kwargs)}
            
            except (TypeError, ValueError, ZeroDivisionError) as error:

                if debug:
                    return {"status": False, "result": str(error)}
                else:
                    return {"status": False, "result": responses.get(type(error), str(error))}
                    
            except (SqliteError) as error:

                # Deshacer los cambios
                if "database" in locals():
                    locals()["database"].rollback()
                    locals()["database"].close()
                
                if debug:
                    return {"status": False, "result": str(error)}
                else:
                    return {"status": False, "result": "Ha ocurrido un error, no se guardaron cambios"}

            except Exception as error:
                return {
                    "status": False,
                    "result": str(error)
                }
        
        return run

    # Verificar si se proporciona la función
    if len(args) == 1 and callable(args[0]):
        return decorator(args[0])
    else:
        return decorator

