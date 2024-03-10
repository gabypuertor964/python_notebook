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

soccer = set()
basketball = set()

def register():

    while True:
    
        title("Crear Matricula",True)
    
        options = [
            "Futbol",
            "Baloncesto"
        ]
        print_options(options)
    
        # Obtener la opcion
        option = get("Seleccione una opcion: ")
    
        # Validar la opcion
        if(is_number(option) and int(option) in range(1,len(options)+2)):
                
            # Opcion: Salir
            if(int(option) == len(options)+1):
                break;
    
            # Opcion: Futbol
            if(int(option) == 1):
                
                space()
                name = get("Ingrese el nombre del jugador: ")
                name = clean_spaces(name.capitalize())
                soccer.add(name)
                
            # Opcion: Baloncesto
            if(int(option) == 2):

                space()
                name = get("Ingrese el nombre del jugador: ")
                name = clean_spaces(name.capitalize())
                basketball.add(name)

def statistics():
    
    while True:

        title("Estadisticas",True)

        options = [
            "Estudiantes inscritos en futbol",
            "Estudiantes inscritos en baloncesto",
            "Estudiantes instritos en ambos deportes",
            "Estudiantes inscritos en un solo deporte",
        ]
        print_options(options)

        option = get("Seleccione una opcion: ")

        if(is_number(option) and int(option) in range(1,len(options)+2)):

            # Opcion: Salir
            if(int(option) == len(options)+1):
                break;

            if(int(option) == 1):
                title("Estadisticas",True)
                print_options(list(soccer),"Estudiantes inscritos en futbol","",False)

                input_skip()

            if(int(option) == 2):
                title("Estadisticas",True)
                print_options(list(basketball),"Estudiantes inscritos en baloncesto","",False)

                input_skip()

            if(int(option) == 3):
                title("Estadisticas",True)

                both = soccer.intersection(basketball)
                print_options(list(both),"Estudiantes inscritos en ambos deportes","",False)

                input_skip()

            if(int(option) == 4):
                title("Estadisticas",True)
                
                soccer_only = soccer.difference(basketball)
                basketball_only = basketball.difference(soccer)

                only_list = soccer_only.union(basketball_only)
                print_options(list(only_list),"Estudiantes inscritos en un solo deporte","",False)

                input_skip()

while True:

    title("Colecciones - Deportes",True)

    subtitle(f"Actualmente hay {len(soccer)} matriculas de futbol y {len(basketball)} matriculas de baloncesto")

    options = [
        "Crear Matricula",
        "Estadisticas"
    ]
    print_options(options)

    # Obtener la opcion
    option = get("Seleccione una opcion: ")

    # Validar la opcion
    if(is_number(option) and int(option) in range(1,len(options)+2)):
        
        # Opcion: Salir
        if(int(option) == len(options)+1):
            break;

        # Opcion: Crear Matricula
        if(int(option) == 1):
            register()

        #Opcion: Estadisticas
        if(int(option) == 2):
            statistics()
