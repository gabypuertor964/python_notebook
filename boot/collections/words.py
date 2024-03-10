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

word_1 = ""
word_2 = ""
list_words = set()

def repeat_search():
    global word_1, word_2

    for x,y in zip(word_1.lower(),word_2.lower()):
    
        if(x == y and x != " "):
            list_words.add(x)

def show_repeated():
    global list_words

    title("Caracteres repetidos",True)

    if(len(list_words) > 0):
        subtitle("Los caracteres repetidos son: ")
        for word in list_words:
            print(indentation(word,True),end="")
    else:
        subtitle("No hay caracteres repetidos")

    print("\n")
    input_skip()

while True:

    while True:
        title("Buscador de caracteres repetidos",True)
        option = get("Ingrese la primera cadena de texto: ")

        if(len(option.strip()) > 0):
            word_1 = option
            break
    
    while True:
        title("Buscador de caracteres repetidos",True)
        option = get("Ingrese la segunda cadena de texto: ")

        if(len(option.strip()) > 0):
            word_2 = option
            break

    repeat_search()
    show_repeated()

    break;
    