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

value = 0
sales = 0
sales_total = 0
discount_total = 0

def generate_discount(age: int, stratum: int):
    
    global value
    global sales
    global sales_total
    global discount_total

    if(stratum == 1 and age < 18):
        percentage = 20
    elif(stratum == 1 and age >= 18):
        percentage = 15
    elif(stratum == 2 and age < 18):
        percentage = 10
    elif(stratum == 2 and age >= 18):
        percentage = 5

    # Calcular el descuento y sumar al total de descuentos
    discount = value * (percentage/100)
    discount_total += discount

    # Calcular el valor final y sumar al total de ventas
    value_before = value - discount
    sales_total += value

    # Imprimir la venta
    title("Venta de boletas", True)

    message = f"""
        * Valor neto: {value}
        * Porcentaje de descuento: {percentage}%
        * Valor del descuento: {discount}
        * Valor final: {value_before}
    """
    print(message)

def add_sale():

    status = True
    stratum = 0
    age = 0

    # Solicitar y almacenar el estrato del comprador
    while status:
        title("Venta de boletas", True)

        options = [
            'Estrato 1',
            'Estrato 2'
        ]
        print_options(options,"¿Que numero de estrato eres?")
        option = get()

        # Validar que el valor recibido sea un numero y este dentro del rango
        if(is_number(option) and int(option) in range(1,len(options)+2)):
            
            # Verificar si se selecciono la opcion de salida
            if(int(option) == len(options)+1):
                status = False
                break

            stratum = int(option)
            break

    # Solicitar y almacenar la edad del comprador
    while status:
        title("Venta de boletas", True)

        option = get("Ingresa tu edad (-1 para salir): ")

        # Validar que el valor recibido sea un numero y este dentro del rango
        if(is_number(option) and int(option) in range(1,100)):

            # Verificar si se selecciono la opcion de salida
            if(int(option) == -1):
                status = False
                break

            age = int(option)
            break

    # Ejectuar el descuento solo en caso de no haber sido cancelada la operacion
    if(status):
        global sales
        sales += 1
        generate_discount(age, stratum)
        input_skip()
        
def set_value():

    # Solicitar y almacenar el valor individual de la boleta
    while True:

        title("Venta de boletas", True)
        option = get("Ingresa el valor de la boleta: ")

        # Validar que el valor recibido sea un numero y este dentro del rango
        if(is_number(option) and int(option) > 0):
                
            # Almacenar el valor de la boleta
            global value
            value = int(option)
            break

def show_info():

    title("Venta de boletas", True)

    message = f"""
        * Valor de la boleta: {value}
        * Ventas realizadas: {sales}
        * Total de ventas: {sales_total}
        * Total de descuentos: {discount_total}
    """
    print(message)

    input_skip()

def validation_value() -> bool:
    
    # Validar que el valor de la boleta haya sido establecido
    if(value == 0):
        title("Venta de boletas", True)
        subtitle("El valor de la boleta no ha sido establecido")
            
        input_skip()
        return False
    else:
        return True

while True:

    title("Venta de boletas", True)

    options = [
        'Establecer valor de la boleta',
        'Registrar venta',
        'Ver Resumen'
    ]
    print_options(options)
    option = get()

    # Validar que el valor recibido sea un numero y este dentro del rango
    if(is_number(option) and int(option) in range(1,len(options)+2)):
        
        # Verificar si se selecciono la opcion de salida
        if(int(option) == len(options)+1):
            break

        # Opcion: Establecer valor de la boleta
        if(int(option) == 1):
            set_value()

        # Opcion: Registrar venta
        if(int(option) == 2):

            # Notificar si el valor de la boleta no ha sido establecido
            if(validation_value()):
                add_sale()
                
        # Opcion: Ver Resumen
        if(int(option) == 3):

            # Notificar si el valor de la boleta no ha sido establecido
            if(validation_value()):
                show_info()