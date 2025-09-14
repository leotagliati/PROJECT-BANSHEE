# main.py
import pygame, sys
from ui_display import menu, game_over
from core_game import run_game

def main():
    pygame.init()

    while True:
        choice = menu()
        if choice == "start":
            score = run_game()
            next_action = game_over(score)
            if next_action == "menu":
                continue
        elif choice == "exit":
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()
