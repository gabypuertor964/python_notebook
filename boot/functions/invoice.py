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
    Para pagar la factura del acueducto es necesario tener en cuenta el estrato social en el que se encuentra el usuario del servicio y de acuerdo con ello dar un subsidio

    Si es de estrato 1 y 2 el usuario tiene un descuento del 50% sobre el valor del servicio siempre que el consumo de agua sea menor a 10 metros cúbicos.
    
    Si es mayor a 10 y menor a 15 solo tiene un subsidio del 40% y si esta entre 16 y 25 metros cubico tendrá un descuento del 25% si es mayor a 25 metros no tendrá descuento.

    Para el estrato 3 tendrá un descuento del 20% solo si el consumo es menor a 10 metros cúbicos.

    El estrato 4 no tiene subsidio.

    Y si es estrato 5 o 6 aporta un 30% del valor de su consumo para subsidiar los estratos 1, 2 y 3

    El valor de la tarifa es de $1500  para el estrato 1 y 2
    Para el estrato 3 es de $2000
    Para el estrato 4 $ 2500 y para los estratos 5 y 6 de $ 3000
    
    Se debe calcular el servicio  del alcantarillado con el 50% del valor del consumo de agua
    Determine el valor que debe cancelar el usuario cada mes
"""
from tools.old.display import *
from tools.old.inputs import *
from tools.old.transform import *

# Generar el valor del impuesto
def tax(value):
    return try_int(float(value) * 0.21)

def inovice(net_value:float):
    
    # Titulo principal
    title("Detallado factura",True)

    subtitle(f"Valor neto: {try_int(net_value)}") 
    subtitle(f"Valor del impuesto: {try_int(tax(net_value))}")

    subtitle(f"Valor total: {try_int(net_value + tax(net_value))}")
    input_skip()

while True:

    # Titulo principal
    title("Valor de factura",True)

    # Obtener el valor neto
    value = get("Ingrese el valor neto (q para salir): ")

    # Limpiar el valor
    value = value.replace("$", "").replace(",", "").replace(".", "")

    # Salir del ciclo
    if(value.lower() == "q"):
        break

    # Verificar si el valor es un numero valido
    if(value.isdigit() and float(value) > 0):
        inovice(float(value))
