import os.path as path
import sys

# Añadir el directorio principal al path
sys.path.append(path.abspath(path.join(path.dirname(__file__), '../../')))

from classes.sqlite import SqLite

# Actualizar el nombre del archivo de la base de datos
SqLite.data_access["route"] = "students.db"

# Habilitar la verificacion de clases foraneas
SqLite.execute("PRAGMA foreign_keys = ON;")

class Student(SqLite):
    
    # Metodo constructor
    def __init__(self, id:int, names: str, surnames: str, age: int):
        super().__init__(id=id, names=names, surnames=surnames, age=age)


    # Creacion de tabla
    @staticmethod
    def create_table():
        return SqLite.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                names TEXT NOT NULL,
                surnames TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        """)


    # Crear una instancia de la clase
    @staticmethod
    def create_instance(id: int, names: str, surnames: str, age: int):
        return Student(id, names, surnames, age)


    # Creacion del estudiante
    @staticmethod
    def create(names: str, surnames: str, age: int):
        return SqLite.execute("INSERT INTO students (names, surnames, age) VALUES (?, ?, ?)", (names, surnames, age))
    

    # Obtener todos los estudiantes
    @staticmethod
    def select():
        response = SqLite.execute("SELECT * FROM students")

        if response["status"] and len(response["result"]) > 0:
            for index, student in enumerate(response["result"], start=0):
                response["result"][index] = Student.create_instance(student[0], student[1], student[2], student[3])

        return response


    # Actualizar un estudiante
    @staticmethod
    def update(student, values: dict = {}):

        names = values.get("names", student.names)
        surnames = values.get("surnames", student.surnames)
        age = values.get("age", student.age)

        return SqLite.execute("UPDATE students SET names = ?, surnames = ?, age = ? WHERE id = ?", (names, surnames, age, student.id))


    # Eliminar un estudiante
    @staticmethod
    def delete(student):
        return SqLite.execute("DELETE FROM students WHERE id = ?", (student.id,))


    # Sobreescribir el metodo str
    def __str__(self):
        return f"{self.names} {self.surnames} - {self.age} años"

class Course(SqLite):

    # Metodo constructor
    def __init__(self, name: str, value: float, duration: int):
        super().__init__(name=name, value=value, duration=duration)

    # Creacion de tabla
    @staticmethod
    def create_table():
        return SqLite.execute("""
            CREATE TABLE IF NOT EXISTS courses(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                value REAL NOT NULL,
                duration INTEGER NOT NULL,
                student_id INTEGER NOT NULL,
                FOREIGN KEY(student_id) REFERENCES students(id)
            )
        """)

    # Crear una instancia de la clase
    @staticmethod
    def create_instance(id: int, name: str, value: float, duration: int):
        return Course(id, name, value, duration)

class Campus(SqLite):

    # Metodo constructor
    def __init__(self, name: str, address: str):
        super().__init__(name=name, address=address)

    # Creacion de tabla
    @staticmethod
    def create_table():
        return SqLite.execute("""
            CREATE TABLE IF NOT EXISTS campus(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL
            )
        """)

# Crear la tabla Campus
Campus.create_table()

# Crear la tabla Student
Student.create_table()

# Crear la tabla Course
Course.create_table()