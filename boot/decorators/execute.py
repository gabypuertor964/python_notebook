import sqlite3

# Ejecutar de forma segura las operaciones
def execute(function):

    # Funcion decorada
    def run(*args, **kwargs):
        try:
            return {
                "status": True,
                "result": function(*args, **kwargs)
            }
        except (TypeError, ValueError):
            return {
                "status": False,
                "result": "Argumentos invalidos"
            }
        except ZeroDivisionError:
            return {
                "status": False,
                "result": "No se puede dividir entre 0"
            }
        except sqlite3.Error:

            # Deshacer los cambios
            if "database" in locals():
                locals()["database"].rollback()
                locals()["database"].close()
            
            return {
                "status": False,
                "result": "Ha ocurrido un error, no se guardaron cambios"
            }
        except Exception as message:
            return {
                "status": False,
                "result": message
            }
    
    return run
