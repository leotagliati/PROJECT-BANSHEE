import pygame
import os
from game_config import HEIGHT, WIDTH

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
    
    
class MotherEnemy:
    def __init__(self, x, y, fire_rate=500, beam_rate=5000, beam_duration=1500):  
        base_path = os.path.dirname(os.path.dirname(__file__))  
        assets_path = os.path.join(base_path, "Assets", "motherShip.png")
        self.image = pygame.image.load(assets_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        
        self.speed = 1
        self.max_health = 100
        self.health = self.max_health
        
        self.fire_rate = fire_rate
        self.beam_rate = beam_rate
        self.beam_duration = beam_duration

        self.last_fire = pygame.time.get_ticks()
        self.last_beam = pygame.time.get_ticks()

        # beam state
        self.beam_active = False
        self.beam_start_time = 0
        self.beam_rect = None

    def update(self, bullets):
        self.move()
        now = pygame.time.get_ticks()

        # tiros normais
        if now - self.last_fire >= self.fire_rate:
            self.shoot(bullets)
            self.last_fire = now

        # beam
        if not self.beam_active and now - self.last_beam >= self.beam_rate:
            self.start_beam()
            self.last_beam = now

        if self.beam_active and now - self.beam_start_time > self.beam_duration:
            self.beam_active = False
            self.beam_rect = None

    def move(self):
        self.rect.y += self.speed  # anda no eixo vertical

        if self.rect.top <= 0:
            self.rect.top = 0
            self.speed = abs(self.speed)  # garante que vai pra baixo

        elif self.rect.bottom >=  HEIGHT:  # usa a altura do jogo
            self.rect.bottom = HEIGHT
            self.speed = -abs(self.speed)  # garante que vai pra cima

    def draw(self, screen):
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

        # desenhar beam se ativo
        if self.beam_active and self.beam_rect:
            pygame.draw.rect(screen, (255, 0, 200), self.beam_rect)  # cor do raio

    def shoot(self, bullets):
        bullets.append(EnemyBullet(self.rect.right - 4, self.rect.centery - 3))

    def start_beam(self):
        self.beam_active = True
        self.beam_start_time = pygame.time.get_ticks()
        # cria um retângulo horizontal gigante
        self.beam_rect = pygame.Rect(
            self.rect.right,  # começa do lado da nave
            self.rect.centery - 10,  # centralizado
            2000,  # largura absurda
            20     # altura do feixe
        )
