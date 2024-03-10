import os
import sys

# Añadir el directorio principal al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Importaciones requeridas
from tools.console.directories import create_route
from decorators.execute import execute
from abc import ABC, abstractmethod
import sqlite3


# Superclase para los Tablas
class Table(ABC):

    # Atributo de clase: Ruta por default de la base de datos
    __route = "database.db"

    @classmethod
    def set_route(cls, route: str) -> None:
        cls.__route = route
    
    # Ejecutar una consulta de forma segura
    @staticmethod
    @execute
    def execute(query: str, parameters: tuple = ()):
        with sqlite3.connect(Table.__route) as database:
            cursor = database.cursor()

            cursor.execute(query, parameters)
            database.commit()

            return cursor.fetchall()


    # Metodo constructor
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


    # Crear la tabla
    @staticmethod
    def create_table(): pass

    # Crear una instancia de la clase
    @staticmethod
    def create_instance(): pass

    # Obtener todos los registros
    @abstractmethod
    def select(self): pass

    # Obtener un registro segun su id
    @abstractmethod
    def get(self, id: int): pass

    # Crea un registro
    @staticmethod
    def create(): pass

    # Actualiza un registro
    @abstractmethod
    def update(self): pass

    # Elimina un registro
    @abstractmethod
    def delete(self): pass
