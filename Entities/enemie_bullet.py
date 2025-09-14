import pygame

class EnemyBullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 6)
        self.speed = 10

    def update(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (243, 87, 73), self.rect)
