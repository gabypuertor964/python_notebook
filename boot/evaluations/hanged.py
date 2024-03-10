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
    Ahorcado: Debes presentar el siguiente menú al usuario
    
        * Agregar Palabra (solicita una palabra y la agregas a una lista de palabras)
        * Configurar (debes preguntar el número de equivocaciones permitidas)
        * Jugar
        * Salir

        La opción 3 de jugar debe obtener una palabra aleatoriamente de la lista de palabras y presentar en pantalla los espacios de cada letra de la palabra seleccionada. Por ejemplo, si la palabra es paciencia, se debe mostrar en pantalla así _ _ _ _ _ _ _ _ _ Posteriormente, debe preguntar una letra al usuario y si la letra se encuentra, debe mostrarla en la posición correcta. Para el caso anterior, si la letra seleccionada es la a, se debería mostrar así _ A _ _ _ _ _ _ A En caso de error debe indicar cuantas oportunidades le quedan para adivinar. El juego termina cuando el usuario llena la palabra antes de terminar sus oportunidades (en ese caso gana) o cuando se terminan sus oportunidades sin llenar la palabra (en ese caso pierde). Al perder o ganar se debe presentar un mensaje indicando cual era la palabra escondida. Usar funciones y gestión de excepciones.
"""
from tools.old.display import *
from tools.old.inputs import *
from tools.old.transform import *
import random

# Listado de palabras unicas
words = set()

# Lista de letras encontradas
letters_found = []

# Lista de letras usadas 
letters = []

# Intentos permitidos
tries = 0

# Configurar el numero de intentos
def configurator():
    
    global tries

    while True:

        # Mostrar el titulo del menu
        title('Configuracion',True)

        # Solicitar el numero de intentos al usuario
        tries = get('Ingrese el numero de intentos permitidos: ')

        # Validar el numero de intentos
        if(tries.isdigit() and int(tries) > 0):

            # Convertir el numero de intentos a entero
            tries = int(tries)

            subtitle('El numero de intentos ha sido configurado')
            break
        else:
            subtitle('El numero de intentos no es valido')

        input_skip()

# Mostrar el listado de palabras
def show_words():
    global words

    # Mostrar el listado de palabras
    title('Listado de palabras',True)

    # Validar si hay palabras registradas
    if(len(words) > 0):

        # Mostrar el listado de palabras
        print_options(list(words),"Palabras registradas","",False)
    else:
        subtitle('No hay palabras registradas')

    input_skip()

# Insertar una palabra
def insert_word():

    global words

    while True:

        # Mostrar el titulo del menu
        title('Agregar palabra',True)

        # Solicitar la palabra al usuario
        word = get('Ingrese la palabra: ')

        # Validar la palabra
        if(word.isalpha() and len(word) > 0):

            # Limpiar y formatear la palabra
            word = str(clean_spaces(word)).lower()

            # Agregar la palabra al listado
            words.add(word)

            subtitle('La palabra ha sido agregada')
            input_skip()
            break
        else:
            subtitle('La palabra no es valida')
            input_skip()

# Seleccionar una palabra aleatoria
def select_word():
    return list(words)[random.randint(0,len(words)-1)]

# Mostrar la palabra
def print_word(word: str):

    global letters

    result = ''

    # Recorrer la palabra y mostrar las letras encontradas de lo contrario mostrar un guion bajo
    for letter in word:
        if(letter in letters):
            result += letter
        else:
            result += '_'
        result += ' '
    
    # Mostrar el resultado
    return result

# Eliminar las palabras
def delete_words():

    title('Eliminar palabras',True)

    global words
    words = set()

    subtitle('Las palabras han sido eliminadas')
    input_skip()

# Jugar
def game():

    global tries, words, letters, letters_found

    # Crear una copia de los intentos permitidos
    tries_in_game = tries

    # Mostrar el titulo principal
    title('Jugar ahorcado',True)

    # Validar si hay palabras registradas
    if(len(words) > 0):

        # Validar si se definio el numero de intentos
        if(tries > 0):
        
            # Obtener la palabra a adivinar
            word = select_word()

            while True:

                # Mostrar el titulo principal
                title('Jugar ahorcado',True)

                # Mostrar la palabra
                text_center(print_word(word))

                # Solicitar una letra al usuario
                letter = get('Ingrese una letra: ')

                # Validar la letra
                if(letter.isalpha()):
                    
                    if(letter not in letters):
                        
                        # Agregar la letra a la lista de letras usadas
                        letters.append(letter)

                        # Validar si la letra se encuentra en la palabra
                        if(letter in word):

                            # Agregar la letra a la lista de letras encontradas
                            letters_found.append(letter)

                            # Validar si el usuario ha ganado
                            if(len(letters_found) == len(set(word))):

                                # Mostrar el titulo principal
                                title('Jugar ahorcado',True)

                                # Mostrar la palabra
                                text_center(print_word(word))

                                # Saltar una linea
                                space()

                                # Mostrar el mensaje de felicitaciones
                                text_center('!FELICIDADES, HAS GANADO¡')
                                input_skip()

                                break
                        else:
                            tries_in_game -= 1

                            # Validar si el usuario ha perdido
                            if(tries_in_game == 0):
                                subtitle(f'Lo siento, has perdido. La palabra era {word}')
                                input_skip()

                                break
                            else:
                                subtitle(f'La letra no se encuentra en la palabra, te quedan {tries_in_game} intentos')
                                input_skip()

                    else:
                        subtitle('La letra ya ha sido usada')
                        input_skip()

                else:
                    subtitle('La letra no es valida')
                    input_skip()
        else:
            subtitle('No se ha configurado el numero de intentos permitidos')
            input_skip()

    else:
        subtitle('No hay palabras registradas')
        input_skip()
    
while True:

    # Mostrar el titulo del menu
    title('Ahorcado',True)

    # Mostrar las opciones del menu y obtener la seleccion del usuario
    options = [
        'Agregar palabra',
        'Ver lista de palabras',
        'Eliminar palabras',
        'Configurar',
        'Jugar',
    ]
    print_options(options)

    # Obtener la seleccion del usuario
    option = get()

    # Validar la seleccion del usuario
    if(option.isdigit() and int(option) in range(1, len(options)+2)):

        # Opcion: Salir
        if(int(option) == len(options)+1):
            break

        # Opcion: Agregar palabra
        if(int(option) == 1):
            insert_word()

        # Opcion: Ver lista de palabras
        elif(int(option) == 2):
            show_words()

        # Opcion: Eliminar palabras
        elif(int(option) == 3):
            delete_words()

        # Opcion: Configurar
        elif(int(option) == 4):
            configurator()

        # Opcion: Jugar
        elif(int(option) == 5):

            # Validar si hay palabras registradas
            game()

            # Reiniciar las variables
            letters_found = []
            letters = []
