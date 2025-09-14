# main.py
import pygame, sys
from ui_display import menu, game_over
from core_game import run_game
from game_config import pin_map
from input_system import InputSystem

def main():
    pygame.init()
    input_system = InputSystem(pin_map)
    while True:
        choice = menu(input_system)
        if choice == "start":
            score = run_game(input_system)
            next_action = game_over(score, input_system)
            if next_action == "menu":
                continue
        elif choice == "exit":
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()
