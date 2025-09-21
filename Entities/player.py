import pygame
import os

class Player:
    def __init__(self,x,y):
        base_path = os.path.dirname(os.path.dirname(__file__))  # sobe até PROJECT-BANSHEE
        assets_path = os.path.join(base_path, "Assets", "playerShip.png")
        self.image = pygame.image.load(assets_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 6
        

    def move(self, actions):
        """
        actions: dict de bools
        exemplo: {"UP": True, "DOWN": False, "LEFT": True, "RIGHT": False} (falso seria pressionado)
        """
        if actions.get("LEFT", False):
            self.rect.x -= self.speed
        if actions.get("RIGHT", False):
            self.rect.x += self.speed
        if actions.get("UP", False):
            self.rect.y -= self.speed
        if actions.get("DOWN", False):
            self.rect.y += self.speed

    def draw(self, screen):
        px, py = self.rect.topleft
        pw, ph = self.rect.size
        screen.blit(self.image, (px, py))
