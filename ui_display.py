import pygame, sys
from game_config import FONT, WIDTH, HEIGHT, screen, clock

def draw_text(text, size, y, color=(255,255,255)):
    f = pygame.font.SysFont("Arial", size)
    surf = f.render(text, True, color)
    rect = surf.get_rect(center=(WIDTH//2, y))
    screen.blit(surf, rect)

def menu(input_system=None):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "  # inclui espaço
    player_name = [""] * 12  # limite de 12 caracteres
    current_index = 0        # posição do cursor no nome
    char_index = 0           # letra selecionada no alfabeto
    cursor_visible = True
    cursor_timer = 0

    while True:
        dt = clock.tick(30)
        cursor_timer += dt
        if cursor_timer >= 500:  # alterna o cursor a cada 500ms
            cursor_visible = not cursor_visible
            cursor_timer = 0

        screen.fill((8, 12, 30))
        draw_text("NANOSTRAY", 40, HEIGHT//2 - 60, (100,200,255))
        draw_text("Digite seu nome:", 28, HEIGHT//2 - 20, (200,200,200))

        display_name = "".join(player_name)
        if cursor_visible:
            display_name = display_name[:current_index] + "|" + display_name[current_index+1:]
        draw_text(display_name or "_", 28, HEIGHT//2 + 20, (255,255,255))

        draw_text("Pressione FIRE para começar", 20, HEIGHT - 80, (160,160,160))
        pygame.display.flip()

        if input_system:
            input_system.update()

            # Navega pelas letras
            if input_system.is_pressed_edge("UP"):
                char_index = (char_index + 1) % len(alphabet)
            if input_system.is_pressed_edge("DOWN"):
                char_index = (char_index - 1) % len(alphabet)

            # Navega pelo índice do nome
            if input_system.is_pressed_edge("RIGHT"):
                if current_index >= 11:
                    current_index = 0
                else: 
                    current_index = min(current_index + 1, 11)
            if input_system.is_pressed_edge("LEFT"):
                current_index = max(current_index - 1, 0)

            # Atribui letra selecionada ao índice atual
            player_name[current_index] = alphabet[char_index]

            # FIRE → inicia o jogo
            if input_system.is_pressed_edge("FIRE"):
                final_name = "".join(player_name).rstrip()
                if final_name.strip() == "":
                    final_name = "Jogador"
                return {"action": "start", "name": final_name}


def game_over(score, input_system=None):
    screen.fill((40, 6, 6))
    draw_text("GAME OVER", 48, HEIGHT//2 - 20, (255,90,90))
    draw_text(f"Score: {score}", 28, HEIGHT//2 + 30, (230,230,230))
    pygame.display.flip()
    pygame.time.delay(2000)

    if input_system:
        input_system.update()
    return "menu"

def display_hud(score):
    score_surf = FONT.render(f"Score: {score}", True, (220,220,220))
    screen.blit(score_surf, (8, 8))
