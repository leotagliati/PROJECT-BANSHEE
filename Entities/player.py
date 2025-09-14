import pygame

class Player:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,40,36)
        self.speed = 4

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self,screen):
        px,py = self.rect.topleft
        pw,ph = self.rect.size
        ship_surf = pygame.Surface((pw, ph), pygame.SRCALPHA)
        pygame.draw.polygon(ship_surf, (60,180,255), [(0, ph//2), (pw, 0), (pw, ph)])
        screen.blit(ship_surf, (px, py))
