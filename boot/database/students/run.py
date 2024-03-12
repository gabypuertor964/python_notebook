import os.path as path
import sys

# Añadir el directorio principal al path
sys.path.append(path.abspath(path.join(path.dirname(__file__), '../../')))

from tools.display.menu import print_menu
from tools.display.titles import title
from tools.display.text_align import left
from tools.input.get import get, wait
from database import *


# Crear un estudiante
def create_student():

    # Diccionario de datos
    data = {}

    # Nombres
    while True:

        # Titulo
        title("Registrar estudiante")

        # Solicitar los nombres
        names = get("Ingrese los nombres (-1 para regresar)")

        # Validar los nombres
        if names.isalpha():
            data["names"] = names
            break
        elif names == "-1":
            return

    # Apellidos
    while True:

        # Titulo
        title("Registrar estudiante")

        # Solicitar los apellidos
        surnames = get("Ingrese los apellidos")

        # Validar los apellidos
        if surnames.isalpha():
            data["surnames"] = surnames
            break

    # Edad
    while True:
            
        # Titulo
        title("Registrar estudiante")
    
        # Solicitar la edad
        age = get("Ingrese la edad")
    
        # Validar la edad
        if age.isdigit() and int(age) > 0:
            data["age"] = int(age)
            break

    # Crear el estudiante
    response = Student.create(data["names"], data["surnames"], data["age"])

    # Imprimir la respuesta
    title("Estado de la operacion")

    # Verificar si el estudiante fue creado
    if response["status"]:
        print(left("El estudiante ha sido registrado con exito", False))
    else:
        print(left("Ha ocurrido un error, el estudiante no ha sido registrado", False))

    wait()


# Listar estudiantes
def list_students():

    # Titulo
    title("Listar estudiantes")

    # Obtener los estudiantes
    response = Student.select()

    # Verificar si la consulta fue exitosa
    if response["status"]:
        
        # Verificar si no se han obtenido estudiantes
        if len(response["result"]) == 0:
            print(left("No se han encontrado estudiantes", False))

        # Imprimir los estudiantes
        for student in response["result"]:
            print(left(str(student), False))
        
    else:
        print(left("Ha ocurrido un error, no se han podido obtener los estudiantes", False))

    wait()


# Actualizar estudiante
def update_student():

    # Titulo
    title("Actualizar estudiante")

    # Listar los estudiantes
    query_select = Student.select()

    # Verificar si la consulta fue exitosa
    if query_select["status"]:
        
        # Verificar si no se han obtenido estudiantes
        if len(query_select["result"]) == 0:

            print(left("No se han encontrado estudiantes", False))
            wait()

            return

        registers = []

        # Crear lista de estudiantes
        for student in query_select["result"]:
            registers.append(f"{student.names} {student.surnames}")
        
        while True:

            # Listar estudiantes
            print_menu(registers, "Estudiantes")

            # Solicitar al usuario que ingrese el id del estudiante
            option = get("Ingrese el numero del estudiante que desea actualizar")

            # Verificar si el la opcion es valida
            if option.isdigit() and int(option) in range(1, len(registers) + 2):

                # Obtener el estudiante
                student = query_select["result"][int(option) - 1]

                # Diccionario de datos
                data = {}

                # Nombres
                while True:

                    # Titulo
                    title("Actualizar estudiante")

                    # Solicitar los nombres
                    names = get("Ingrese los nombres (-1 para dejar el valor actual)")

                    # Validar los nombres
                    if names.isalpha():
                        data["names"] = names
                        break
                    elif names == "-1":
                        break

                # Apellidos
                while True:

                    # Titulo
                    title("Actualizar estudiante")

                    # Solicitar los apellidos
                    surnames = get("Ingrese los apellidos (-1 para dejar el valor actual)")

                    # Validar los apellidos
                    if surnames.isalpha():
                        data["surnames"] = surnames
                        break
                    elif surnames == "-1":
                        break

                # Edad
                while True:
                            
                    # Titulo
                    title("Actualizar estudiante")
                    
                    # Solicitar la edad
                    age = get("Ingrese la edad (-1 para dejar el valor actual)")
                    
                    # Validar la edad
                    if age.isdigit() and int(age) > 0:
                        data["age"] = int(age)
                        break
                    elif age == "-1":
                        break

                # Actualizar el estudiante
                response = student.update(student, data)

                # Imprimir la respuesta
                title("Estado de la operacion")

                # Verificar si el estudiante fue actualizado
                if response["status"]:
                    print(left("El estudiante ha sido actualizado con exito", False))
                else:
                    print(left("Ha ocurrido un error, el estudiante no ha sido actualizado", False))

                wait()

                break

    else:
        print(left("Ha ocurrido un error, no se han podido obtener los estudiantes", False))
        wait()


# Eliminar estudiante
def delete_student():
    # Titulo
    title("Eliminar estudiante")

    # Listar los estudiantes
    query_select = Student.select()

    # Verificar si la consulta fue exitosa
    if query_select["status"]:
        
        # Verificar si no se han obtenido estudiantes
        if len(query_select["result"]) == 0:
            print(left("No se han encontrado estudiantes", False))
            wait()
            return

        registers = []

        # Crear lista de estudiantes
        for student in query_select["result"]:
            registers.append(f"{student.names} {student.surnames}")
        
        while True:

            # Listar estudiantes
            print_menu(registers, "Estudiantes")

            # Solicitar al usuario que ingrese el id del estudiante
            option = get("Ingrese el numero del estudiante que desea eliminar")

            # Verificar si el la opcion es valida
            if option.isdigit() and int(option) in range(1, len(registers) + 2):

                # Obtener el estudiante
                student = query_select["result"][int(option) - 1]

                # Eliminar el estudiante
                response = student.delete(student)

                # Imprimir la respuesta
                title("Estado de la operacion")

                # Verificar si el estudiante fue eliminado
                if response["status"]:
                    print(left("El estudiante ha sido eliminado con exito", False))
                else:
                    print(left("Ha ocurrido un error, el estudiante no ha sido eliminado", False))

                wait()

                break

    else:
        print(left("Ha ocurrido un error, no se han podido obtener los estudiantes", False))
        wait()


# Gestion de estudiantes
def students_manager():
    
    while True:
        
        # Titulo
        title("Gestion de estudiantes")

        # Opciones
        menu = [
            "Registrar",
            "Listar",
            "Actualizar",
            "Eliminar",
        ]

        # Imprimir el menu
        print_menu(menu)

        # Solicitar al usuario que ingrese una opcion
        option = get("Ingrese una opcion")

        # Validar la opcion
        if option.isdigit() and int(option) in range(1, len(menu) + 2):

            # Convertir la opcion a entero
            option = int(option)

            # Opcion salir
            if option == len(menu) + 1:
                break

            # Registrar estudiante
            if option == 1:
                create_student()

            # Listar estudiantes
            elif option == 2:
                list_students()

            # Actualizar estudiante
            elif option == 3:
                update_student()

            # Eliminar estudiante
            elif option == 4:
                delete_student()


# Crear un curso
def create_course():

    # Diccionario de datos
    data = {}

    # Nombre
    while True:

        # Titulo
        title("Registrar curso")

        # Solicitar el nombre
        name = get("Ingrese el nombre del curso (-1 para regresar)")

        # Validar el nombre
        if name.isalpha():
            data["name"] = name
            break
        elif name == "-1":
            return

    # Descripcion
    while True:

        # Titulo
        title("Registrar curso")

        # Solicitar la descripcion
        description = get("Ingrese la descripcion")

        # Validar la descripcion
        if description.isalpha():
            data["description"] = description
            break

    # Crear el curso
    response = Course.create(data["name"], data["description"])

    # Imprimir la respuesta
    title("Estado de la operacion")

    # Verificar si el curso fue creado
    if response["status"]:
        print(left("El curso ha sido registrado con exito", False))
    else:
        print(left("Ha ocurrido un error, el curso no ha sido registrado", False))

    wait()


# Listar cursos
def list_courses():

    # Titulo
    title("Listar cursos")

    # Obtener los cursos
    response = Course.select()

    # Verificar si la consulta fue exitosa
    if response["status"]:
        
        # Verificar si no se han obtenido cursos
        if len(response["result"]) == 0:
            print(left("No se han encontrado cursos", False))

        # Imprimir los cursos
        for course in response["result"]:
            print(left(str(course), False))
        
    else:
        print(left("Ha ocurrido un error, no se han podido obtener los cursos", False))

    wait()


# Actualizar curso
def update_course():

    # Titulo
    title("Actualizar curso")

    # Listar los cursos
    query_select = Course.select()

    # Verificar si la consulta fue exitosa
    if query_select["status"]:
        
        # Verificar si no se han obtenido cursos
        if len(query_select["result"]) == 0:

            print(left("No se han encontrado cursos", False))
            wait()

            return

        registers = []

        # Crear lista de cursos
        for course in query_select["result"]:
            registers.append(course.name)
        
        while True:

            # Listar cursos
            print_menu(registers, "Cursos")

            # Solicitar al usuario que ingrese el id del curso
            option = get("Ingrese el numero del curso que desea actualizar")

            # Verificar si el la opcion es valida
            if option.isdigit() and int(option) in range(1, len(registers) + 2):

                # Obtener el curso
                course = query_select["result"][int(option) - 1]

                # Diccionario de datos
                data = {}

                # Nombre
                while True:

                    # Titulo
                    title("Actualizar curso")

                    # Solicitar el nombre
                    name = get("Ingrese el nombre del curso (-1 para dejar el valor actual)")

                    # Validar el nombre
                    if name.isalpha():
                        data["name"] = name
                        break
                    elif name == "-1":
                        data["name"] = course.name
                        break

                # Descripcion
                while True:

                    # Titulo
                    title("Actualizar curso")

                    # Solicitar la descripcion
                    description = get("Ingrese la descripcion (-1 para dejar el valor actual)")

                    # Validar la descripcion
                    if description.isalpha():
                        data["description"] = description
                        break
                    elif description == "-1":
                        data["description"] = course.description
                        break

                # Actualizar el curso
                response = course.update(course, data)

                # Imprimir la respuesta
                title("Estado de la operacion")

                # Verificar si el curso fue actualizado
                if response["status"]:
                    print(left("El curso ha sido actualizado con exito", False))
                else:
                    print(left("Ha ocurrido un error, el curso no ha sido actualizado", False))

                wait()

                break

    else:
        print(left("Ha ocurrido un error, no se han podido obtener los cursos", False))
        wait()


# Eliminar curso
def delete_course():
    # Titulo
    title("Eliminar curso")

    # Listar los cursos
    query_select = Course.select()

    # Verificar si la consulta fue exitosa
    if query_select["status"]:
        
        # Verificar si no se han obtenido cursos
        if len(query_select["result"]) == 0:
            print(left("No se han encontrado cursos", False))
            wait()
            return

        registers = []

        # Crear lista de cursos
        for course in query_select["result"]:
            registers.append(course.name)
        
        while True:

            # Listar cursos
            print_menu(registers, "Cursos")

            # Solicitar al usuario que ingrese el id del curso
            option = get("Ingrese el numero del curso que desea eliminar")

            # Verificar si el la opcion es valida
            if option.isdigit() and int(option) in range(1, len(registers) + 2):

                # Obtener el curso
                course = query_select["result"][int(option) - 1]

                # Eliminar el curso
                response = course.delete(course)

                # Imprimir la respuesta
                title("Estado de la operacion")

                # Verificar si el curso fue eliminado
                if response["status"]:
                    print(left("El curso ha sido eliminado con exito", False))
                else:
                    print(left("Ha ocurrido un error, el curso no ha sido eliminado", False))

                wait()

                break

    else:
        print(left("Ha ocurrido un error, no se han podido obtener los cursos", False))
        wait()


# Gestion de cursos
def courses_manager():
    
    while True:
        
        # Titulo
        title("Gestion de cursos")

        # Opciones
        menu = [
            "Registrar",
            "Listar",
            "Actualizar",
            "Eliminar",
        ]

        # Imprimir el menu
        print_menu(menu)

        # Solicitar al usuario que ingrese una opcion
        option = get("Ingrese una opcion")

        # Validar la opcion
        if option.isdigit() and int(option) in range(1, len(menu) + 2):

            # Convertir la opcion a entero
            option = int(option)

            # Opcion salir
            if option == len(menu) + 1:
                break

            # Registrar curso
            if option == 1:
                create_course()

            # Listar cursos
            elif option == 2:
                list_courses()

            # Actualizar curso
            elif option == 3:
                update_course()

            # Eliminar curso
            elif option == 4:
                delete_course()


# Gestion de sedes
def campus_manager():
    pass


# Gestion de matriculas
def enrollments_manager():
    pass


# Hilo principal
while True:

    # Imprimir el titulo principal
    title("Sena Sofia Plus")

    # Opciones
    menu = [
        "Estudiantes",
        "Cursos",
        "Sedes",
        "Matriculas",
    ]

    # Imprimir el menu
    print_menu(menu)

    # Solicitar al usuario que ingrese una opcion
    option = get("Ingrese una opcion")

    # Validar la opcion
    if option.isdigit() and int(option) in range(1, len(menu) + 2):

        # Convertir la opcion a entero
        option = int(option)

        # Opcion salir
        if option == len(menu) + 1:
            break

        # Gestion de estudiantes
        if option == 1:
            students_manager()
        
        # Gestion de cursos
        elif option == 2:
            courses_manager()
        
        # Gestion de sedes
        elif option == 3:
            campus_manager()

        # Gestion de matriculas
        elif option == 4:
            enrollments_manager()
    