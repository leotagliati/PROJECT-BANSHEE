import pygame

class BasicEnemy:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,40,36)
        self.speed = 2
        self.max_health = 15
        self.health = self.max_health
        
    def move(self):
        self.rect.x -= self.speed

    def draw(self,screen):
        px,py = self.rect.topleft
        pw,ph = self.rect.size
        ship_surf = pygame.Surface((pw, ph), pygame.SRCALPHA)
        pygame.draw.polygon(ship_surf, (255, 0, 0), [(0, ph//2), (pw, 0), (pw, ph)])
        screen.blit(ship_surf, (px, py))
        
        # --- Barra de vida ---
        if self.health >= 1:
            bar_width = pw
            bar_height = 5
            fill = int((self.health / self.max_health) * bar_width)
            pygame.draw.rect(screen, (255,0,0), (px, py - 8, bar_width, bar_height))
            pygame.draw.rect(screen, (0,255,0), (px, py - 8, fill, bar_height))  