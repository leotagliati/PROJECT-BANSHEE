import pygame

pygame.init()

WIDTH, HEIGHT = 800, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 24)

pin_map = {
    10: "UP",
    9: "DOWN",
    20: "LEFT",
    27: "RIGHT",
    17: "FIRE"
}