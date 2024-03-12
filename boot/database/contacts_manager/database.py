import os.path as path
import sys

# Añadir el directorio principal al path
sys.path.append(path.abspath(path.join(path.dirname(__file__), '../../')))

# Importaciones requeridas
from classes.sqlite import SqLite

# Tabla: Contactos/contacts
class Contact(SqLite):

    # Actualizar la ruta de la base de datos
    SqLite.data_access["route"] = "contacts.db"

    # Crear la tabla
    @staticmethod
    def create_table():
        return SqLite.execute("""
            CREATE TABLE IF NOT EXISTS contacts(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                names TEXT NOT NULL,
                surnames TEXT NOT NULL,
                phone INTEGER NOT NULL
            )
        """)


    # Crear una instancia de la clase
    @staticmethod
    def create_instance(id: int, names: str, surnames: str, phone: int):
        return Contact(id, names, surnames, phone)


    # Obtener todos los contactos
    @staticmethod
    def select():

        # Ejecutar la consulta
        response = SqLite.execute("SELECT * FROM contacts")

        # Verificar si la consulta fue exitosa y se obtuvieron registros
        if response["status"] and len(response["result"]) > 0:

            # Crear una lista de contactos
            for index, contact in enumerate(response["result"], start=0):
                response["result"][index] = Contact.create_instance(contact[0], contact[1], contact[2], contact[3])

        # Retornar la respuesta
        return response
    
        
    # Obtener un contacto
    @staticmethod
    def get(id: int):
        return SqLite.execute("SELECT * FROM contacts WHERE id = ?", (id,))


    # Crear un contacto
    @staticmethod
    def create(names: str, surnames: str, phone: int):
        return SqLite.execute("INSERT INTO contacts (names, surnames, phone) VALUES (?, ?, ?)", (names, surnames, phone))


    # Actualizar un contacto
    def update(self, values: dict = {}):

        # Declarar valores por defecto
        names = values.get("names", self.names)
        surnames = values.get("surnames", self.surnames)
        phone = values.get("phone", self.phone)

        return SqLite.execute("UPDATE contacts SET names = ?, surnames = ?, phone = ? WHERE id = ?", (names, surnames, phone, self.id))
    

    # Eliminar un contacto
    def delete(self):
        return SqLite.execute("DELETE FROM contacts WHERE id = ?", (self.id,))


    # Metodo constructor
    def __init__(self, id: int, names: str, surnames: str, phone: int):

        # Ejecucion de metodo padre
        super().__init__(id=id, names=names, surnames=surnames, phone=phone)
