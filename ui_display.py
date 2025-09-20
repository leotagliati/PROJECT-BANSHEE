import pygame, sys
from game_config import FONT, WIDTH, HEIGHT, screen, clock

def draw_text(text, size, y, color=(255,255,255)):
    f = pygame.font.SysFont("Arial", size)
    surf = f.render(text, True, color)
    rect = surf.get_rect(center=(WIDTH//2, y))
    screen.blit(surf, rect)

def menu(input_system=None):
    while True:
        clock.tick(60)
        screen.fill((8, 12, 30))
        draw_text("NANOSTRAY", 40, HEIGHT//2 - 60, (100,200,255))
        pygame.display.flip()

        if input_system:
            input_system.update()
            # input_system.debug_print_buttons()

        # for e in pygame.event.get():
        #     if e.type == pygame.QUIT:
        #         pygame.quit(); sys.exit()
        #     if e.type == pygame.KEYDOWN:
        #         if e.key == pygame.K_RETURN:
        #             return "start"
        #         if e.key == pygame.K_ESCAPE:
        #             return "exit"

        # --- Verifica botões do Raspberry Pi ---
            if input_system.is_pressed_edge("FIRE"):  # botão para "start"
                return "start"
            if input_system.is_pressed("EXIT"):  # opcional, botão para sair
                return "exit"

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
