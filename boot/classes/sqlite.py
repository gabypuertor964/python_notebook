import os
import sys

# Añadir el directorio principal al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Importaciones requeridas
from decorators.execute import execute
from classes.model import Model
import sqlite3

# Clase para operacion con SQLite
class SqLite(Model):

    # Atributo de clase: Ruta por default de la base de datos
    data_access = {"route": "database.db"}

    # Ejecutar una consulta de forma segura
    @staticmethod
    @execute(debug=True)
    def execute(query: str, parameters: tuple = ()):
        with sqlite3.connect(SqLite.data_access["route"]) as database:
            cursor = database.cursor()

            cursor.execute(query, parameters)
            database.commit()

            return cursor.fetchall()

