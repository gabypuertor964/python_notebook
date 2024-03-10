import os.path as path 
import sys

# Añadir el directorio principal al path
sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

from tools.display.titles import title
from tools.display.text_align import left
from tools.display.menu import print_menu
from tools.input.get import get, wait
from tools.input.clean import trim_spaces
from tools.input.transform import float_or_int

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

# Inicializar variables
stratum = use = 0

# Listado de tarifas
tariffs = {
    1: 1500,
    2: 1500,
    3: 2000,
    4: 2500,
    5: 3000,
    6: 3000
}

# Solicitar y almacenar el estrato
def set_stratum() -> None:

    # Usar variable global
    global stratum

    while True:

        # Titulo
        title('Definir estrato')

        # Solicitar el estrato
        value = get("Ingrese el estrato (1 - 6) (q para salir)")

        # Limpiar la cadena
        value = trim_spaces(value)

        # Verificar opcion salir
        if(value.lower() == 'q'):
            break

        # Verificar el valor ingresado
        if(value.isdigit() and int(value) in range(1, 7)):

            # Almacenar el estrato
            stratum = int(value)

            title('Informacion')
            print(f"{left(f"El numero de estrato ha sido definido como {value}", False)} \n")

            wait()
            break
        else:
            title('Advertencia')
            print(f"{left('El valor ingresado no es valido', False)} \n")
            wait()

# Solicitar y almacenar el consumo
def set_use() -> None:

    # Usar variable global
    global use

    while True:

        # Titulo
        title('Definir consumo')

        # Solicitar el consumo
        value = get("Ingrese el consumo de agua (m3) (q para salir)")

        # Limpiar la cadena
        value = trim_spaces(value)

        # Verificar opcion salir
        if(value.lower() == 'q'):
            break

        # Verificar el valor ingresado
        if(value.isdigit() and int(value) > 0):

            # Almacenar el consumo
            use = int(value)

            title('Informacion')
            print(f"{left(f"El consumo de agua ha sido definido como {value} m3", False)} \n")

            wait()
            break
        else:
            title('Advertencia')
            print(f"{left('El valor ingresado no es valido', False)} \n")
            wait()

# Calcular el porcentaje de descuento
def calculate_disscount() -> int:

    # Estrato 1 y 2
    if(stratum in range(1,3)):
        if(use < 10):
            return 50
        elif(use in range(10,15)):
            return 40
        elif(use in range(16,26)):
            return 25
        else:
            return 0
    
    # Estrato 3
    elif(stratum == 3):
        if(use < 10):
            return 20
        else:
            return 0
    
    # Estrato 4
    elif(stratum == 4):
        return 0
    
    # Estrato 5 y 6
    elif(stratum in range(5,7)):
        return 30

# Calcular la factura
def facturation() -> None:
    
    # Obtener el porcentaje de descuento
    disscount = calculate_disscount()

    # Obtener la tarifa base segun el estrato
    tariff = tariffs[stratum]

    # Validar si el descuento es a favor o en contra del usuario
    if(stratum in range(1,5)):
        
        # Calcular el valor sin descuento de la factura
        net_value = tariff * use

        # Aplicar el descuento
        value_disscount = net_value * (disscount / 100)

        # Calcular el valor final de la factura
        value = net_value - value_disscount

        # Simbolo del descuento
        symbol = "-"
    else:
        # Calcular el valor sin descuento de la factura
        net_value = tariff * use

        # Aplicar el cobro adicional por subsidio a otros estratos
        value_disscount = net_value / (disscount / 100)

        # Calcular el valor final de la factura
        value = net_value + value_disscount

        # Simbolo del descuento
        sumbol = "+"

    # Calcular el valor del alcantarillado y sumarlo al valor total
    sewage = value * 0.5
    value += sewage

    # Visualizar la factura
    title('Facturacion EAAB')
    print(f"""
        Estrato: {stratum}
        Consumo: {use} m3

        Tarifa base: ${float_or_int(net_value)}
        Descuento: {symbol} {float_or_int(disscount)}%

        Valor Alcantarillado: ${float_or_int(sewage)}

        Valor neto: ${float_or_int(net_value)}
        valor descuento: {symbol} ${float_or_int(value_disscount)}

        Total a pagar: ${float_or_int(value)}
    """)
    wait()

# Hilo principal
while True:
    
    # Titulo
    title('Factura EAAB')

    # Listado de opciones del menu
    options = [
        'Definir estrato',
        'Definir consumo',
        'Calcular factura',
    ]

    # Mostrar menu
    print_menu(options, "Seleccione una opcion", True, "Salir")

    # Obtener la opcion del usuario
    option = get()
    
    # Verificar si la opcion es valida
    if(trim_spaces(option).isdigit() and int(option) in range(1, len(options) + 2)):

        # Opcion: Salir
        if(int(option) == len(options) + 1):
            break

        # Opcion: Definir estrato
        if(int(option) == 1):
            set_stratum()

        # Opcion: Definir consumo
        if(int(option) == 2):
            set_use()

        # Opcion: Calcular factura
        if(int(option) == 3):
            
            if(stratum > 0 and use > 0):
                facturation()
            else:
                title('Advertencia')

                print(f"{left("Por favor defina el estrato y el consumo de agua antes de calcular la factura", False)} \n")
                wait()
