import os.path as path 
import sys

# Añadir el directorio principal al path
sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

"""
    Piedra papel o tijera: Debes preguntar al usuario una opción entre piedra, papel o tijera y una vez ingresada su opción se debe mostrar la opción ingresada por el usuario y la obtenida de manera aleatoria por el computador. El programa debe indicar el ganador con base en las siguientes reglas: Piedra gana a Tijera, Tijera gana a Papel, Papel gana a Piedra. En caso de Empatado se debe continuar hasta que haya un ganador. Utiliza funciones.
"""
from tools.old.display import *
from tools.old.inputs import *
from tools.old.transform import *
import random

# Movimientos
movements = [
    "Piedra",
    "Papel",
    "Tijera"
]

# Generar un movimiento aleatorio
def generate_movement():
    return movements[random.randint(0, len(movements)-1)]

def win_or_lose(user, computer) -> dict:

    # Escenario: Empatado
    if(user == computer):
        return {
            "status": "Empatado",
            "message": f"El usuario y el computador eligieron {user}"
        }
    
    # Escenario: Usuario -> Piedra y Computador -> Tijera
    elif(user == "Piedra" and computer == "Tijera"):
        return {
            "status": "Ganado",
            "message": f"El usuario eligió {user} y el computador eligió {computer}"
        }
    
    # Escenario: Usuario -> Tijera y Computador -> Papel
    elif(user == "Tijera" and computer == "Papel"):
        return {
            "status": "Ganado",
            "message": f"El usuario eligió {user} y el computador eligió {computer}"
        }
    
    # Escenario: Usuario -> Papel y Computador -> Piedra
    elif(user == "Papel" and computer == "Piedra"):
        return {
            "status": "Ganado",
            "message": f"El usuario eligió {user} y el computador eligió {computer}"
        }

    # Escenario: Usuario -> Tijera y Computador -> Piedra
    else:
        return {
            "status": "Perdido",
            "message": f"El usuario eligió {user} y el computador eligió {computer}"
        }

while True:

    # Obtener la opción del usuario
    title("Piedra, papel o tijera",True)

    print_options(movements,"Elije un movimiento","",False)
    option = get("Opcion: ")

    if(option.isdigit() and int(option) in range(1,len(movements)+1)):

        # Obtener la opción del usuario
        title("Piedra, papel o tijera",True)
        
        # Obtener el movimiento del usuario
        user = movements[int(option)-1]

        # Mostrar el movimiento del usuario
        print(indentation(f"El usuario eligió {user}",True))

        # Generar el movimiento del computador
        computer = generate_movement()

        # Mostrar el movimiento del computador
        print(indentation(f"El computador eligió {computer}",True),end="\n\n")

        # Determinar el ganador
        result = win_or_lose(user,computer)

        # Mostrar el resultado
        print(indentation(result["message"],True))
        print(indentation(f"Has {result["status"]}",True),end="\n\n")
        
        input_skip()

        if(result["status"] == "Ganado"):
            break

# Obtener la opción del usuario
title("Piedra, papel o tijera",True)

# Mostrar el mensaje de felicitaciones
subtitle("Felicidades has ganado")

# Esperar
input_skip()