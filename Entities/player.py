import pygame

class Player:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,40,36)
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
        ship_surf = pygame.Surface((pw, ph), pygame.SRCALPHA)
        pygame.draw.polygon(ship_surf, (60,180,255), [(pw, ph//2), (0, 0), (0, ph)])
        screen.blit(ship_surf, (px, py))
