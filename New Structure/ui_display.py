# ui_display.py
import pygame, sys
from game_config import FONT, WIDTH, HEIGHT, screen, clock

def draw_text(text, size, y, color=(255,255,255)):
    f = pygame.font.SysFont("Arial", size)
    surf = f.render(text, True, color)
    rect = surf.get_rect(center=(WIDTH//2, y))
    screen.blit(surf, rect)

def menu():
    while True:
        clock.tick(60)
        screen.fill((8, 12, 30))
        draw_text("NANOSTRAY - SIDE", 40, HEIGHT//2 - 60, (100,200,255))
        draw_text("ENTER para Jogar | Arrows mover | Espaço atira", 20, HEIGHT//2, (200,200,200))
        draw_text("ESC para sair", 18, HEIGHT//2 + 40, (180,180,180))
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    return "start"
                if e.key == pygame.K_ESCAPE:
                    return "exit"

def game_over(score):
    screen.fill((40, 6, 6))
    draw_text("GAME OVER", 48, HEIGHT//2 - 20, (255,90,90))
    draw_text(f"Score: {score}", 28, HEIGHT//2 + 30, (230,230,230))
    pygame.display.flip()
    pygame.time.delay(2000)
    return "menu"

def display_hud(score):
    score_surf = FONT.render(f"Score: {score}", True, (220,220,220))
    screen.blit(score_surf, (8, 8))
