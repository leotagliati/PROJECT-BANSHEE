import pygame
import os

class PlayerBullet:
    def __init__(self, x, y):
        base_path = os.path.dirname(os.path.dirname(__file__))
        assets_path = os.path.join(base_path, "Assets", "playerBullet.png")
        self.image = pygame.image.load(assets_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 10

    def update(self):
        self.rect.x += self.speed

    def draw(self, screen):
        px, py = self.rect.topleft
        screen.blit(self.image, (px, py))    
        
class EnemyBullet:
    def __init__(self, x, y):
        base_path = os.path.dirname(os.path.dirname(__file__)) 
        assets_path = os.path.join(base_path, "Assets", "enemyBullet.png")
        self.image = pygame.image.load(assets_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

    def update(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        px, py = self.rect.topleft
        screen.blit(self.image, (px, py))    
