import pygame

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 6)
        self.speed = 10

    def update(self):
        self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 230, 90), self.rect)
