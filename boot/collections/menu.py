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
from tools.old.transform import *

data = set()

def create_list():

    while True:
        title("Crear lista", True)

        option = get("Ingrese el valor a añadir (q para salir): ")
        
        # Verificar si se desea salir
        if(option == 'q'):
            break

        data.add((option.strip()).lower())

def short_list():

    data_tmp = list(data)
    data_tmp.sort(reverse=True)
    show_list(data,"Lista ordenada")

def show_list(data,title_text:str = "Lista original",):
    title(title_text, True)
    
    for index, value in enumerate(data):
        subtitle(f"{index+1}. {value}")

    input_skip()

def average_list():

    global data
    title("Promedio de la lista", True)

    if(is_number_list(data)):

        list_number = []

        for value in data:
            list_number.append(try_int(value))
        
        average = sum(list_number) / len(list_number)
        subtitle(f"El promedio de la lista es: {average}")
        input_skip()
    else:
        subtitle("La lista debe contener solo numeros")
        input_skip()

def search_element():

    title("Buscar elemento", True)
    search = get("Ingrese el elemento a buscar (q para salir): ")

    print("\n")

    search = search.lower()
    found = False

    for index, value in enumerate(data):
        if(value == search):
            subtitle(f"El elemento {search} se encuentra en la posicion {index}")
            found = True
    
    if(not found):
        subtitle(f"El elemento {search} no se encuentra en la lista")

    input_skip()

while True:

    title("Aplicaciones con Listas",True)

    options = [
        "Ingresar lista nueva",
        "Ordenar lista",
        "Promedio lista",
        "Buscar elemento",
        "Ver lista original"
    ]
    print_options(options, "Seleccione una opcion")
    option = get("Opcion: ")

    if(is_number(option) and int(option) > 0 and int(option) in range(1,len(options)+2)):

        # Veririficar si la opcion es salir
        if(int(option) == len(options)+1):
            break

        # Opcion: Añadir elementos
        if(int(option) == 1):
            data.clear()
            create_list()

        # Opcion: Ordenar lista
        if(int(option) == 2):
            short_list()

        # Opcion: Promedio lista
        if(int(option) == 3):
            average_list()

        # Opcion: Buscar elemento
        if(int(option) == 4):
            search_element()

        # Opcion: Ver lista original
        if(int(option) == 5):
            show_list(data)