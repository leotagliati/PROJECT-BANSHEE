import pygame
from dotenv import load_dotenv
import os

pygame.init()

WIDTH, HEIGHT = 800, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 24)

load_dotenv()
apiKey = os.getenv("API_KEY")

pin_map = {
    10: "UP",
    9: "DOWN",
    20: "LEFT",
    27: "RIGHT",
    17: "FIRE"
}