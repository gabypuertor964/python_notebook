import os
import sys

# Añadir el directorio principal al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from classes.model import Model
from decorators.execute import execute
import pymysql

# Clase para operacion con PyMySQL
class PyMySQL(Model):

    # Atributo de clase: Atributos por default
    data_access = {
        "host": "localhost",
        "user": "root",
        "password": "",
        "database": ""
    }

    # Ejecutar una consulta de forma segura
    @staticmethod
    @execute
    def execute(query: str, parameters: tuple = ()):
        with pymysql.connect(
            host=pymysql.data_access["host"],
            user=pymysql.data_access["user"],
            password=pymysql.data_access["password"],
            db=pymysql.data_access["database"]
        ) as database:
            cursor = database.cursor()

            cursor.execute(query, parameters)
            database.commit()

            return cursor.fetchall()
