import os.path as path 
import sys

# Añadir el directorio principal al path
sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

from tools.display.titles import title
from tools.display.menu import *
from tools.input.get import *
from tools.input.verify import is_numbers, is_positive
from tools.display.text_align import left
from random import randint


# Declaracion clase jugador
class player:

    # Metodo constructor
    def __init__(self, name: str):
        self.name: str = name
        self.score: int = 0

    # Metodo para actualizar el puntaje
    def update_score(self, score: int) -> None:
        self.score += score

    # Metodo para validar si dos jugadores son iguales
    def __eq__(self, other) -> bool:
        if isinstance(other, player):
            return self.name == other.name
        
        return False

# Inicializar el diccionario de jugadores
players = []

# Patrones de dados
patterns = [

    # Sextetos
    {"structure" : {1: 6},"score" : 3000},
    {"structure" : {2: 6},"score" : 3000},
    {"structure" : {3: 6},"score" : 3000},
    {"structure" : {4: 6},"score" : 3000},
    {"structure" : {5: 6},"score" : 3000},
    {"structure" : {6: 6},"score" : 3000},

    # Tres pares
    {"structure" : {1: 3, 2: 3},"score" : 2500},
    {"structure" : {1: 3, 3: 3},"score" : 2500},
    {"structure" : {1: 3, 4: 3},"score" : 2500},
    {"structure" : {1: 3, 5: 3},"score" : 2500},
    {"structure" : {1: 3, 6: 3},"score" : 2500},

    {"structure" : {2: 3, 3: 3},"score" : 2500},
    {"structure" : {2: 3, 4: 3},"score" : 2500},
    {"structure" : {2: 3, 5: 3},"score" : 2500},
    {"structure" : {2: 3, 6: 3},"score" : 2500},

    {"structure" : {3: 3, 4: 3},"score" : 2500},
    {"structure" : {3: 3, 5: 3},"score" : 2500},
    {"structure" : {3: 3, 6: 3},"score" : 2500},

    {"structure" : {4: 3, 5: 3},"score" : 2500},
    {"structure" : {4: 3, 6: 3},"score" : 2500},

    {"structure" : {5: 3, 6: 3},"score" : 2500},

    # Quintetos
    {"structure" : {1: 5},"score" : 2000},
    {"structure" : {2: 5},"score" : 2000},
    {"structure" : {3: 5},"score" : 2000},
    {"structure" : {4: 5},"score" : 2000},
    {"structure" : {5: 5},"score" : 2000},
    {"structure" : {6: 5},"score" : 2000},

    # Escalera
    {"structure" : {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1},"score" : 1500},

    # Cuartetos
    {"structure" : {1: 4},"score" : 1000},
    {"structure" : {2: 4},"score" : 1000},
    {"structure" : {3: 4},"score" : 1000},
    {"structure" : {4: 4},"score" : 1000},
    {"structure" : {5: 4},"score" : 1000},
    {"structure" : {6: 4},"score" : 1000},

    # Trios
    {"structure" : {1: 3},"score" : 100},
    {"structure" : {2: 3},"score" : 200},
    {"structure" : {3: 3},"score" : 300},
    {"structure" : {4: 3},"score" : 400},
    {"structure" : {5: 3},"score" : 500},
    {"structure" : {6: 3},"score" : 600},
]

# Buscador de patrones
def search_pattern(dices: list) -> dict:
    # Ordenar los dados
    dices.sort()

    score = 0
    farkle = True

    # Iterar sobre cada patrón en el diccionario patterns
    for pattern in patterns:
        # Inicializar un diccionario con la cantidad de cada número en los dados
        dice_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        for dice in dices:
            dice_counts[dice] += 1

        # Almacenar los datos del patron
        structure = pattern["structure"]
        score_pattern = pattern["score"]
        match = True

        for digit, count in structure.items():
            if dice_counts.get(digit, 0) < count:
                match = False
                break

        if match:
            score += score_pattern
            farkle = False

            # Eliminar los dados correspondientes al patrón encontrado
            for digit, count in structure.items():
                for _ in range(count):
                    dices.remove(digit)
            break

    # Contar la cantidad de 1 y 5 restantes
    count_1 = dices.count(1)
    count_5 = dices.count(5)

    # Sumar el puntaje de los 1 y 5 restantes
    if count_1 > 0:
        score += count_1 * 100
        farkle = False
    if count_5 > 0:
        score += count_5 * 50
        farkle = False

    return {"farkle": farkle, "score": score}

# Valdar si el nombre del jugador es unico
def unique_name(name: str) -> bool:

    for player in players:
        if player.name == name:
            return False
        
    return True

# Registrar un jugador
def register_player() -> None:
    
    # Usar variables globales
    global players

    while True: 

        # Titulo
        title("Registrar jugador")

        # Obtener el nombre del jugador
        name = get("Ingrese el nombre del jugador (-1 para cancelar)")

        # Validar si el nombre es -1
        if (name.isdigit() and int(name) == -1):
            break

        # Capitalizar el nombre
        name = name.capitalize()

        # Validar si el nombre ya existe
        if unique_name(name) == False:

            # Mostrar advertencia
            title("Advertencia")
            print(left(f"El nombre {name} ya existe, por favor ingrese otro nombre \n", False))

            wait()
        elif len(name) == 0:
                
            # Mostrar advertencia
            title("Advertencia")
            print(left("El nombre no puede estar vacio, por favor ingrese un nombre \n", False))
    
            wait()
        else:

            # Agregar el jugador a la lista
            players.append(player(name))

            # Mostrar mensaje de exito
            title("Felicidades")
            print(left(f"El jugador {name} ha sido registrado con exito \n", False))

            wait()
            break

# Mostrar los jugadores registrados
def show_players() -> None:
    
    # Titulo
    title("Jugadores registrados")

    # Validar si hay jugadores registrados
    if len(players) > 0:
        
        # Inicializar una sublista de jugadores
        list_players = []

        # Insertar los nombres jugadores en la sublista
        for player in players:
            list_players.append(player.name)

        # Imprimir la lista de jugadores
        print_menu(list_players, "Jugadores registrados",False)
    else:
        print(left("No hay jugadores registrados \n"))

    wait()

# Eliminar jugadores
def delete_players() -> None:
    
    while True:
        # Titulo
        title("Eliminar jugadores")

        # Opciones disponibles
        options = [
            "Si",
            "No"
        ]
        print_menu(options, "¿Estas seguro de eliminar a todos los jugadores?", False)

        # Obtener la opcion
        option = get()

        # Validar si la opcion es valida
        if option.isdigit() and int(option) in range(1, len(options) + 2):

            if int(option) == 1:

                # Limpiar la lista de jugadores
                players.clear()

                # Mostrar mensaje de exito
                title("Felicidades")
                print(left("Los jugadores han sido eliminados con exito \n", False))

                wait()
                break
            else:
                break

# Ronda de juego
def round_player() -> int:
    
    # Numero inicial de dados
    dices = 6

    # Puntaje de la ronda
    score = 0

    # Ciclo de juego
    while True:

        # Titulo
        title("Ronda de juego")

        # Mostrar el numero de dados y el puntaje actual
        print(left(f"Dados disponibles: {dices}", False))
        print(left(f"Puntaje actual: {score}", False), end="\n\n")

        # Initializar las opciones
        options = []

        # Restriccion: Solo se puede lanzar los dados si hay al menos 1 dado
        if dices > 0: 
            options.append("Lanzar los dados")

        # Restriccion: Solo se puede retirar si el puntaje es mayor o igual a 300
        if score >= 300:
            options.append("Guardar y retirarse")

        print_menu(options, "Seleccione", False)

        # Obtener la opcion
        option = get()

        # Validar si la opcion es valida
        if option.isdigit() and int(option) in range(1, len(options) + 2):

            # Opcion 1: Lanzar los dados
            if int(option) == 1:

                # Lanzar los dados
                dice_list = release(dices)

                while True:

                    # Preguntar al usuario que dados desea guardar
                    while True:

                        # Visualizar los dados lanzados
                        title("Dados lanzados")
                        print(left("Tus dados fueron:", False), end=" "); print({f"Dado {i+1}": value for i, value in enumerate(dice_list)})

                        dices_save = get("¿Qué dados deseas guardar? (separados por comas)")

                        # Sobre escribir la variable dices_save con los datos separados por comas
                        dices_save = dices_save.split(",")

                        # Validar si los datos son numeros y positivos
                        if is_numbers(dices_save) and is_positive(dices_save) and len(dices_save) <= dices:
                            break
                        else:
                            title("Advertencia")
                            print(left("Debe seleccionar al menos un dado y estos deben ser números positivos.", False), end="\n\n")

                            wait()

                    # Inicializar la lista de dados a enviar
                    send = []

                    try:

                        # Iterar sobre los indices de los datos a guardar y agregarlos a la lista de datos a enviar
                        for index in dices_save:
                            send.append(dice_list[int(index) - 1])

                        # Buscar el patron de los dados (Si existe)
                        summary = search_pattern(send)

                        # Validar si se hizo farkle
                        if summary["farkle"]:
                            title("Advertencia")

                            print(left("¡Farkle! No has obtenido ningún punto en esta tirada. ¡Inténtalo de nuevo en la próxima ronda!", False), end="\n\n")
                            wait()

                            return 0
                                
                        else:
                            
                            # Actualizar el puntaje
                            score += summary["score"]

                            # Actualizar el numero de dados
                            dices = dices - len(send)

                            break  # Salir del ciclo while interior

                    except IndexError or ValueError:
                        title("Advertencia")
                        print(left("Uno o mas indices no son validos", False), end="\n\n")
                        wait()

            # Opcion 2: Retirarse
            if int(option) == 2:
                return score


# Obtener el jugador con el puntaje mas alto
def player_high_score() -> player:
    return max(players, key=lambda player: player.score)

# Jugar 
def play() -> None:

    # Usar variables globales
    global players

    # Variable de control para hay ganador
    there_winner = False

    # Validar si hay al menos 2 jugadores
    if len(players) >= 2:

        # Ciclo de 10 rondas
        for round in range(1, 11):

            # Ciclo de juego x participante
            for player in players:

                # Titulo
                title(f"Ronda {round}")

                # Mostrar el jugador actual
                print(left(f"Jugador actual: {player.name} \n", False))
                wait()

                # Ejecutar la ronda del jugador y obtener el puntaje
                score = round_player()

                # Titulo
                title("Puntaje de la ronda")

                # Mostrar el puntaje de la ronda
                print(left(f"El jugador {player.name} ha obtenido {score} puntos en la ronda {round} \n", False))
                wait()

                # Actualizar el puntaje del jugador
                player.update_score(score)

                # Titulo
                title("Puntaje de la ronda")

                # Imprimir el puntaje del jugador
                print(left(f"Puntaje total de {player.name}: {player.score} \n", False))
                wait()

                # Validar si el jugador alcanzo o supero los 10000 puntos
                if player.score >= 10000:
                    title("Felicidades")

                    print(left(f"El jugador {player.name} ha ganado la partida \n", False))
                    wait()

                    there_winner = True
                    break

        # Mostrar mensaje de fin del juego en caso de no haber ganador
        if there_winner == False:
            title("Fin del juego")

            # Obtener el jugador con el puntaje mas alto
            player_winner = player_high_score()

            # Mostrar el jugador con el puntaje mas alto y su puntaje
            print(left(f"El jugador con el puntaje mas alto es: {player_winner.name}, con un puntaje de -> {player_winner.score} puntos", False))
            wait()
        
    else:
        title("Advertencia")
        print(left("Se requieren al menos 2 participantes para jugar", False))

        wait()

# Lanzamiento de dados (n dados)
def release(dice: int) -> list:
    # Crear una lista de dados
    dice_list = []

    # Lanzar los dados
    for _ in range(dice):
        dice_list.append(randint(1, 6))

    # Retornar la lista de dados
    return dice_list

# Hilo principal
while True:

    # Titulo principal
    title("Farkle")

    # Listado de opciones
    options = [
        "Registrar jugador",
        "Ver jugadores registrados",
        "Eliminar jugadores",
        "Jugar",
    ]

    # Imprimir el menu
    print_menu(options)

    # Obtener la opcion
    option = get()

    # Validar si la opcion es valida
    if option.isdigit() and int(option) in range(1, len(options) + 2):

        # Opcion n + 1: Salir
        if int(option) == len(options) + 1:
            break

        # Opcion 1: Registrar jugador
        if int(option) == 1:
            register_player()

        # Opcion 2: Ver jugadores registrados
        if int(option) == 2:
            show_players()

        # Opcion 3: Eliminar jugadores
        if int(option) == 3:
            delete_players()

        # Opcion 4: Jugar
        if int(option) == 4:
            play()
