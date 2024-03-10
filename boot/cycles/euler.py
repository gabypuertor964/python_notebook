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

def fact(n):
    # Caso base: el factorial de 0 es 1
    if n == 0:
        return 1
    else:
        # Caso recursivo: n! = n * (n-1)!
        try:
            return n * fact(n - 1)
        except:
            factorial = 1
            for i in range(1, n + 1):
                factorial *= i
            return factorial

def euler_aprox(n):
    # Inicializar la aproximación de Euler
    e_approx = 1

    # Calcular la serie de Taylor para la aproximación de Euler
    for i in range(1, n + 1):
        e_approx += 1 / fact(i)

    # Devolver el resultado de la aproximación
    return e_approx

# Ajustar el valor de n para obtener una mejor aproximación
n = 100
resultado = euler_aprox(n)

# Mostrar el titulo del ejercicio
title("Euler", True)

# Mostrar el resultado de la aproximación
subtitle(f"Aproximación de Euler con {n} términos: {resultado}")
input_skip()
