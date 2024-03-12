import os.path as path
import sys

# Añadir el directorio principal al path
sys.path.append(path.abspath(path.join(path.dirname(__file__), '../../')))

"""
    Run: Menu dinamico de ejecucion de los scripts
"""
from tools.old.display import print_options
from tools.display.titles import title, bye
from tools.input.get import get
import subprocess

themes = {
    'Condicionales': {
        'Tinder': 'boot/conditionals/tinder.py',
        'Motor': 'boot/conditionals/motor.py',
        'Universidad': 'boot/conditionals/university.py',
        'Control de Calidad': 'boot/conditionals/quality_control.py',
    },
    'Ciclos': {
        'Tabla de Multiplicar' : 'boot/cycles/multiplication_table.py',
        'Partido de futbol': 'boot/cycles/soccer.py',
        'Password Verify': 'boot/cycles/password_verify.py',
        'Primos': 'boot/cycles/primes.py',
        'Euler': 'boot/cycles/euler.py',
    },
    'Colecciones': {
        'Deletreador de palabra': 'boot/collections/read_word.py',
        'Pares de palabras': 'boot/collections/peers.py',
        'Insertar Numeros': 'boot/collections/insert_numbers.py',
        'Buscar letras repetidas': 'boot/collections/words.py',
        'Aplicaciones con lista': 'boot/collections/menu.py',
        'Frase' : 'boot/collections/tuples.py',
        'Deportes': 'boot/collections/sports.py',
        'Traductor': 'boot/collections/translator.py',
    },
    'Funciones': {
        'Clasificador de numeros': 'boot/functions/even_or_odd.py',
        'Contador de letras': 'boot/functions/repeat_letter.py',
        'Generador de numeros pares (Recursivo)': 'boot/functions/even_recursive.py',
        'Convertir numero a texto': 'boot/functions/convert_text.py',
        'Obtener caracter de seguridad': 'boot/functions/dni.py',
        'Valor total de la factura': 'boot/functions/invoice.py',
        'Area de un circulo': 'boot/functions/circle.py',
        'Division de dos numeros': 'boot/functions/division.py',
        'Peso de envio': 'boot/functions/weight.py',
    },
    'Excepciones': {
        'Posicion de lista': 'boot/exceptions/position_list.py',
        'Insertar en lista': 'boot/exceptions/insert_list.py',
    },
    'Modulos': {
        "Calculadora": "boot/modules/calculator/run.py",
        "Importacion de varios modulos": "boot/modules/run.py",
    },
    'Evaluaciones': {
        'EEAB': 'boot/evaluations/eaab.py',
        'Pierdra, Papel o Tijera': 'boot/evaluations/rock_paper_scissors.py',
        'Ahorcado': 'boot/evaluations/hanged.py',
        'Farkle': 'boot/evaluations/farkle.py',
    },
    'Clases': {
        'Estudiante': 'boot/classes/student.py',
    },
}

def print_suboptions(options: dict):

    # Mostrar el titulo del menu
    title('Notebook Gaby Puerto',True)

    # Mostrar las opciones del menu y obtener la seleccion del usuario
    print_options(options, "Seleccione un ejercicio")
    option = get()

    # Validar la opcion ingresada
    if(option.isdigit() and int(option) in range(1, len(options)+2)):

        # Verificar si la opcion es salir
        if(int(option) == len(options)+1):
            return
        
        # Obtener el nombre del ejercicio seleccionado
        key = list(options.keys())[int(option)-1]

        subprocess.run(['python', options[key]])

# Impresion y seleccion del menu principal
while True:

    # Mostrar el titulo del menu
    title('Notebook Gaby Puerto')

    # Mostrar las opciones del menu y obtener la seleccion del usuario
    print_options(themes, "Seleccione un tema","Finalizar Ejecucion")
    option = get()

    # Verificar que la opcion ingresada sea valida
    if(option.isdigit() and int(option) in range(1, len(themes)+2)):

        # Verificar si la opcion es salir
        if(int(option) == len(themes)+1):
            bye()
            break;

        # Obtener el nombre del tema seleccionado
        key = list(themes.keys())[int(option)-1]

        # Visualizar el sub-menu de la opcion seleccionada
        print_suboptions(themes[key])
