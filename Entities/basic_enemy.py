import pygame

class BasicEnemy:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,40,36)
        self.speed = 2
        self.health = 1
        
    def move(self):
        self.rect.x -= self.speed

    def draw(self,screen):
        px,py = self.rect.topleft
        pw,ph = self.rect.size
        ship_surf = pygame.Surface((pw, ph), pygame.SRCALPHA)
        pygame.draw.polygon(ship_surf, (255, 0, 0), [(0, ph//2), (pw, 0), (pw, ph)])
        screen.blit(ship_surf, (px, py))