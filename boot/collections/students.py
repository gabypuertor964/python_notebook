"""
    Registrar la ruta del proyecto en el path de python
"""
def root_directory():

    # Importar los modulos requeridos
    import os
    import sys

    # Obtener la ruta del proyecto
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Agregar la ruta del proyecto al path de python
    sys.path.append(project_path)
root_directory()

from tools.old.display import *
from tools.old.inputs import *

students = {}

def get_document():

    while True: 

        title("Informacion del estudiante",True)

        # Consultar el numero de documento
        document = get("Ingrese el numero de documento: ")

        if(is_number(document) and int(document) in range(1,9999999999)):
            return int(document)
            
def get_name():

    while True: 

        title("Informacion del estudiante",True)

        # Consultar
        name = get("Ingrese nombre: ")

        if(not is_number(name)):
            return name

def get_age():
    
    while True: 
    
        title("Informacion del estudiante",True)
    
        # Consultar
        edad = get("Ingrese la edad: ")
    
        if(is_number(edad) and int(edad) in range(1,101)):
            return int(edad)

def get_calification():
        
    while True: 
        
        title("Informacion del estudiante",True)
        
        # Consultar
        calification = get("Ingrese la calificacion: ")
        
        if(is_number(calification) and int(calification) in range(1,11)):
            return int(calification)

while True:

    # Titulo principal
    title("Registro de estudiantes",True)

    options = [
        "Registrar estudiante",
        "Listado de estudiantes",
        "Consultar estudiante segun numero de documento",
    ]
    print_options(options)
    option = get("Seleccione una opcion: ")

    if(is_number(option) and int(option) in range(1,len(options)+2)):
        
        # Opcion: Salir
        if(int(option) == len(options)+1):
            break

        # Opcion: Registrar estudiante
        if(int(option) == 1):

            # Registrar estudiante
            document = get_document()
            name = get_name()
            age = get_age()
            calification = get_calification()

            students[document] = {
                "name": name,
                "age": age,
                "calification": calification
            }

            subtitle(f"El estudiante {name} con documento {document} ha sido registrado")

            input_skip()

        # Opcion: Listado de estudiantes
        if(int(option) == 2):

            # Listado de estudiantes
            title("Listado de estudiantes",True)

            for document, student in students.items():
                subtitle(f"Documento: {document}, Nombre: {student['name']}, Edad: {student['age']}, Calificacion: {student['calification']}")
        
            input_skip()

        # Opcion: Consultar estudiante segun numero de documento
        if(int(option) == 3):

            # Consultar estudiante segun numero de documento
            document = get_document()

            if(document in students):
                student = students[document]
                subtitle(f"Documento: {document}, Nombre: {student['name']}, Edad: {student['age']}, Calificacion: {student['calification']}")
            else:
                subtitle(f"El estudiante con documento {document} no se encuentra registrado")

            input_skip()
