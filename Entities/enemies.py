import pygame
import os

from Entities.bullets import EnemyBullet

class BasicEnemy:
    def __init__(self,x,y):
        base_path = os.path.dirname(os.path.dirname(__file__))
        assets_path = os.path.join(base_path, "Assets", "enemyBasicShip.png")
        self.image = pygame.image.load(assets_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1
        self.max_health = 3
        self.health = self.max_health

    def update(self):
        self.move()
    
    def move(self):
        self.rect.x -= self.speed

    def draw(self,screen):
        px,py = self.rect.topleft
        pw,ph = self.rect.size
        screen.blit(self.image, (px, py))

        
        # --- Barra de vida ---
        if self.health >= 1:
            bar_width = pw
            bar_height = 5
            fill = int((self.health / self.max_health) * bar_width)
            pygame.draw.rect(screen, (255,0,0), (px, py - 8, bar_width, bar_height))
            pygame.draw.rect(screen, (0,255,0), (px, py - 8, fill, bar_height))

class ShooterEnemy:
    def __init__(self, x, y, fire_rate=2000):  # fire_rate em ms
        base_path = os.path.dirname(os.path.dirname(__file__))  # sobe até PROJECT-BANSHEE
        assets_path = os.path.join(base_path, "Assets", "enemyShooterShip.png")
        self.image = pygame.image.load(assets_path).convert_alpha()
        # self.image = pygame.image.load("Assets/enemyShooterShip.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1
        self.max_health = 3
        self.health = self.max_health
        self.fire_rate = fire_rate
        self.last_fire = pygame.time.get_ticks()
        
    def update(self, bullets):
        self.move()
        
        now = pygame.time.get_ticks()
        if now - self.last_fire >= self.fire_rate:
            self.shoot(bullets)
            self.last_fire = now
             
    def move(self):
        self.rect.x -= self.speed

    def draw(self,screen):
        px,py = self.rect.topleft
        pw,ph = self.rect.size
        screen.blit(self.image, (px, py))
        
        # --- Barra de vida ---
        if self.health >= 1:
            bar_width = pw
            bar_height = 5
            fill = int((self.health / self.max_health) * bar_width)
            pygame.draw.rect(screen, (255,0,0), (px, py - 8, bar_width, bar_height))
            pygame.draw.rect(screen, (0,255,0), (px, py - 8, fill, bar_height))

    def shoot(self, bullets):
        bullets.append(EnemyBullet(self.rect.right - 4, self.rect.centery - 3))
        