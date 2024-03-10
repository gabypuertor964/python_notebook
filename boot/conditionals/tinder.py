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

"""
    Tinder: Crear un buscador de parejas permitiendo ingresar las siguientes opciones:

    * Soltera, linda de 20 años, mala persona
    * Soltera, fea de 45 años, buena persona
    * Soltera, linda de 31 años, mala persona
    * Casada, linda de 25 años, buena persona
"""
from tools.old.display import *
from tools.old.inputs import *

persons = []

# Registrar n personas
def add_person():

    person = {}

    # Estado Civil
    while True:
        title('Registro de personas',True)

        options = [
            "Soltera",
            "Casada"
        ]
        print_options(options,"Estado civil")

        # Obtener la opcion del usuario
        option = get()

        # Verificar que la opcion ingresada sea valida
        if(is_number(option)):

            # Verificar si la opcion es regresar
            if(int(option) == 3):
                return
            
            # Verificar que la opcion este dentro del rango
            if(int(option) in [1, 2, 3]):
                person['civil_status'] = options[int(option)-1]
                break
            
    # Apariencia
    while True:
        title('Registro de personas',True)

        options = [
            "Linda",
            "Fea"
        ]

        print_options(options,"Apariencia")

        # Obtener la opcion del usuario
        option = get()

        # Verificar que la opcion ingresada sea valida
        if(is_number(option)):

            # Verificar si la opcion es regresar
            if(int(option) == 3):
                return

            # Verificar que la opcion este dentro del rango
            if(int(option) in [1, 2, 3]):
                person['appearance'] = options[int(option)-1]
                break
    
    # Edad
    while True:
        title('Registro de personas',True)

        # Obtener la opcion del usuario
        age = get("Ingrese la edad (-1 para regresar): ")

        # Verificar que la opcion ingresada sea valida
        if(is_number(age)):

            # Verificar si la opcion es regresar
            if(int(age) == -1):
                return
            
            # Verificar que la edad este en un rango valido
            if(int(age) < 100 and int(age) > 18):

                person['age'] = int(age)
                break
    
    # Buena persona o mala persona
    while True:
        title('Registro de personas',True)

        options = [
            "Buena persona",
            "Mala persona"
        ]

        print_options(options,"Personalidad")

        # Obtener la opcion del usuario
        option = get()

        # Verificar que la opcion ingresada sea valida
        if(is_number(option)):

            # Verificar si la opcion es regresar
            if(int(option) == 3):
                return

            # Verificar que la opcion este dentro del rango
            if(int(option) in [1, 2, 3]):
                person['personality'] = options[int(option)-1]
                break

    # Insertar el registro en la lista de personas
    persons.append(person)

def show_persons(list_persons: list = persons, message: str = "No hay personas registradas"):
    title('Listado de personas',True)

    if(len(list_persons) > 0):
        for person in list_persons:

            message = f"""
                Estado civil:   {person['civil_status']}
                Apariencia:     {person['appearance']}
                Edad:           {person['age']}
                Personalidad:   {person['personality']}
            """
            print(message)
    else:
        subtitle(message)

    input_skip()

# Buscar pareja segun los criterios ingresados
def search():
    
    # Copiado de la lista de personas
    persons_copy = persons.copy()

    # Eliminacion de personas casadas
    persons_copy = [
        person for person in persons_copy if person['civil_status'] != "Casada"
    ]

    if(len(persons_copy) > 0):

        # Obtener el tipo de aparencia deseada y filtrar la lista de personas
        while True:
            title('Buscador de pareja',True)

            options = [
                "Linda",
                "Fea"
            ]
            print_options(options,"Apariencia deseada")

            # Obtener la opcion del usuario
            option = get()

            # Verificar que la opcion ingresada sea valida
            if(is_number(option) and int(option) in [1, 2, 3]):

                # Verificar si la opcion es regresar
                if(int(option) == 3):
                    return

                # Filtrar la lista de personas
                persons_copy = [
                    person for person in persons_copy if person['appearance'] == options[int(option)-1]
                ]

                break

        # Obtener el rango de edad deseada y filtrar la lista de personas
        while True:
            title('Buscador de pareja',True)

            # Obtener la opcion del usuario
            age_min = get("Ingrese la edad minima deseada (-1 para regresar): ")
            age_max = get("Ingrese la edad maxima deseada (-1 para regresar): ")

            # Verificar que los datos ingresados sean validos
            if(is_number_list([age_min,age_max])):

                # Verificar si se ha ingresado la opcion de regresar
                if(int(age_min) == -1 or int(age_max) == -1):
                    return
            
                # Filtrar la lista de personas
                persons_copy = [
                    person for person in persons_copy if person['age'] >= int(age_min) and person['age'] <= int(age_max)
                ]

                break

        # Obtener el tipo de personalidad deseada y filtrar la lista de personas
        while True:
            title('Buscador de pareja',True)

            options = [
                "Buena persona",
                "Mala persona"
            ]
            print_options(options,"Personalidad deseada")

            # Obtener la opcion del usuario
            option = get()

            # Verificar que la opcion ingresada sea valida
            if(is_number(option) and int(option) in [1, 2, 3]):

                # Verificar si la opcion es regresar
                if(int(option) == 3):
                    return

                # Filtrar la lista de personas
                persons_copy = [
                    person for person in persons_copy if person['personality'] == options[int(option)-1]
                ]

                break

        show_persons(persons_copy,"Ups, no se encontraron personas con esas caracteristicas")
    else:
        title('Listado de personas',True)
        subtitle("Ups, no hay personas disponibles")
        input_skip()

# Inicializador de opciones 
while True:

    clean_console()
    title('Bienvenido a tinder')

    # Mostrar el numero de personas registradas
    subtitle(f"Actualmente hay {len(persons)} personas registradas")

    options = [
        "Agregar persona",
        "Ver personas",
        "Buscar pareja"
    ]
    print_options(options,"Ingrese una opcion")

    # Obtener la opcion del usuario
    option = get()

    # Verificar que la opcion ingresada sea valida
    if(is_number(option)):

        # Verificar si la opcion esta dentro del rango
        if(int(option) in [1, 2, 3, 4]):
            if(int(option) == 1):
                add_person()
            elif(int(option) == 2):
                show_persons()
            elif(int(option) == 3):
                search()
            else:
                break