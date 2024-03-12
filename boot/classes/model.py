import os
import sys

# Añadir el directorio principal al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Importaciones requeridas
from abc import ABC, abstractmethod

# Superclase para las operaciones en BD
class Model(ABC):

    # Informacion de conexion
    data_access: dict

    # Ejecutar una consulta de forma segura
    @abstractmethod
    def execute(): pass

    # Metodo constructor
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    # Crear la tabla
    @abstractmethod
    def create_table(): pass

    # Crear una instancia de la clase
    @abstractmethod
    def create_instance(): pass

    # Obtener todos los registros
    @abstractmethod
    def select(): pass

    # Obtener un registro segun su id
    @abstractmethod
    def get(id: int): pass

    # Crea un registro
    @abstractmethod 
    def create(): pass

    # Actualiza un registro
    @abstractmethod
    def update(self): pass

    # Elimina un registro
    @abstractmethod
    def delete(self): pass
