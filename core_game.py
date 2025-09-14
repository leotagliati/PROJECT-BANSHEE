import pygame, random, sys
from game_config import WIDTH, HEIGHT, screen, clock
from ui_display import display_hud
from Entities.player import Player
from Entities.basic_enemy import BasicEnemy
from Entities.bullet import Bullet

def run_game():
    # --- Instâncias ---
    player = Player(50, HEIGHT//2)
    bullets = []
    enemies = []

    # Timer inimigos
    enemy_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(enemy_timer, 900)

    # Fundo: estrelas
    stars = [[random.randrange(0, WIDTH), random.randrange(0, HEIGHT), random.uniform(0.3, 1.2)] for _ in range(120)]
    bg_base_speed = 2.2

    score = 0
    last_shot = 0
    shot_delay = 200  # ms

    running = True
    while running:
        dt = clock.tick(60)

        # --- Eventos ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == enemy_timer:
                y = random.randint(10, HEIGHT - 40)
                enemies.append(BasicEnemy(WIDTH + 10, y))

        keys = pygame.key.get_pressed()

        # --- Player ---
        player.move(keys)
        player.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT-30))

        # --- Tiros ---
        now = pygame.time.get_ticks()
        if keys[pygame.K_SPACE] and now - last_shot >= shot_delay:
            bullets.append(Bullet(player.rect.right + 4, player.rect.centery - 3))
            last_shot = now

        # --- Fundo ---
        for s in stars:
            s[0] -= bg_base_speed * s[2]
            if s[0] < 0:
                s[0] += WIDTH
                s[1] = random.randrange(0, HEIGHT)

        # --- Atualiza balas ---
        for b in bullets[:]:
            b.update()
            if b.rect.left > WIDTH:
                bullets.remove(b)

        # --- Atualiza inimigos ---
        for e in enemies[:]:
            e.move()
            if e.rect.right < 0 or e.rect.top > HEIGHT + 50 or e.rect.bottom < -50:
                enemies.remove(e)

        # --- Colisões balas x inimigos ---
        for b in bullets[:]:
            hit = None
            for e in enemies:
                if b.rect.colliderect(e.rect):
                    hit = e
                    break
            if hit:
                bullets.remove(b)
                e.health -= 1
                if e.health <= 0:
                    enemies.remove(hit)
                    score += 10

        # --- Colisão inimigo x player ---
        for e in enemies:
            if e.rect.colliderect(player.rect):
                return score 

        # --- Desenho ---
        screen.fill((6, 8, 18))
        for s in stars:
            r = 1 if s[2] < 0.6 else (2 if s[2] < 1.0 else 3)
            pygame.draw.circle(screen, (200,200,255), (int(s[0]), int(s[1])), r)

        player.draw(screen)
        for b in bullets:
            b.draw(screen)
        for e in enemies:
            e.draw(screen)

        display_hud(score)
        pygame.display.flip()
