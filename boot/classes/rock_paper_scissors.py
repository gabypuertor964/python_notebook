from abc import ABC, abstractmethod
import random
import os.path as path 
import sys

# Añadir el directorio principal al path
sys.path.append(path.abspath(path.join(path.dirname(__file__), '..')))

from tools.console.clean import clean

class Game(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def display_score(self):
        pass
    
    @abstractmethod
    def end(self):
        pass

class RockPaperScissors(Game):
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0

    def start(self):
        print("Bienvenido a Rock, Paper, Scissors!")

    def display_score(self):
        print("Puntuación del jugador:", self.player_score)
        print("Puntuación de la computadora:", self.computer_score)

    def end(self):
        print("¡Gracias por jugar Piedra, Papel, Tijeras!")

    def play_round(self):
        choices = ['piedra', 'papel', 'tijeras']
        player_choice = input("Ingresa tu opción (piedra/papel/tijeras): ").lower()
        computer_choice = random.choice(choices)
        print("La computadora elige:", computer_choice)
        
        if player_choice == computer_choice:
            print("¡Es un empate!")
        elif (player_choice == 'piedra' and computer_choice == 'tijeras') or \
             (player_choice == 'papel' and computer_choice == 'piedra') or \
             (player_choice == 'tijeras' and computer_choice == 'papel'):
            print("¡Ganaste esta ronda!")
            self.player_score += 1
        else:
            print("¡La computadora gana esta ronda!")
            self.computer_score += 1

    def play_game(self):
        self.start()
        while True:

            # Limpiar la consola
            clean()

            self.display_score()
            self.play_round()
            if input("¿Quieres jugar de nuevo? (yes/no): ").lower() != 'yes':
                break
        self.end()

game = RockPaperScissors()
game.play_game()