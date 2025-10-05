import pygame, random, sys
from game_config import WIDTH, HEIGHT, screen, clock, pin_map
from ui_display import display_hud
from Entities.player import Player
from Entities.enemies import BasicEnemy, ShooterEnemy, MotherEnemy
from Entities.bullets import PlayerBullet, EnemyBullet
from spawn_system import SpawnSystem

def run_game(input_system=None, player_name=None):
    # --- Instâncias ---
    player = Player(50, HEIGHT//2)
    playerBullets = []
    enemiesBullets = []
    enemies = []
    spawn_system = SpawnSystem(30)

    # Timer inimigos
    enemy_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(enemy_timer, 900)

    # Timer para boss (30 segundos)
    boss_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(boss_timer, 30000)  # 30.000 ms = 30s

    # Fundo: estrelas
    stars = [[random.randrange(0, WIDTH), random.randrange(0, HEIGHT), random.uniform(0.3, 1.2)] for _ in range(120)]
    bg_base_speed = 2.2

    score = 0
    last_shot = 0
    shot_delay = 200  # ms

    running = True
    while running:
        dt = clock.tick(60)
        
        input_system.update()
        
        actions = {
            "UP": input_system.is_pressed("UP"),
            "DOWN": input_system.is_pressed("DOWN"),
            "LEFT": input_system.is_pressed("LEFT"),
            "RIGHT": input_system.is_pressed("RIGHT")
        }

        # --- Eventos ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == enemy_timer:
                enemy = spawn_system.spawn_enemy() 
                if enemy:
                    enemies.append(enemy) # só adiciona se couber no budget

            if event.type == boss_timer:
                # Spawn do boss e bloqueia mobs normais
                boss = MotherEnemy(WIDTH-60, HEIGHT/2)
                enemies.append(boss)
                spawn_system.budget = -999
                pygame.time.set_timer(enemy_timer, 0)  # desliga spawns de mobs
                pygame.time.set_timer(boss_timer, 0)   # desliga o timer do boss

        # --- Player ---
        player.move(actions)
        player.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT-30))

        # --- Tiros player ---
        now = pygame.time.get_ticks()
        if input_system.is_pressed("FIRE") and now - last_shot >= shot_delay:
            playerBullets.append(PlayerBullet(player.rect.right + 4, player.rect.centery - 3))
            last_shot = now

        # --- Ações inimigos ---
        for e in enemies:
            if isinstance(e, BasicEnemy):
                e.update()
            if isinstance(e, ShooterEnemy):
                e.update(enemiesBullets)
            if isinstance(e, MotherEnemy):
                e.update(enemiesBullets)

        # --- Fundo ---
        for s in stars:
            s[0] -= bg_base_speed * s[2]
            if s[0] < 0:
                s[0] += WIDTH
                s[1] = random.randrange(0, HEIGHT)

        # --- Atualiza balas ---
        for b in playerBullets[:]:
            b.update()
            if b.rect.left > WIDTH:
                playerBullets.remove(b)

        for b in enemiesBullets[:]:
            b.update()
            if b.rect.x < 0:  # saiu da tela
                enemiesBullets.remove(b)
                
        # --- Atualiza inimigos ---
        for e in enemies[:]:
            e.move()
            if e.rect.right < 0 or e.rect.top > HEIGHT + 50 or e.rect.bottom < -50:
                enemies.remove(e)

        # Colisão balas -> inimigos
        for b in playerBullets[:]:
            for e in enemies[:]:
                if b.rect.colliderect(e.rect):
                    e.health -= 1
                    playerBullets.remove(b)
                    if e.health <= 0:
                        enemies.remove(e)
                        if not isinstance(e, MotherEnemy):  # boss não dá budget
                            spawn_system.add_budget(3)
                        score += 10
                    break
        
        # Colisão balas inimigos -> player
        for b in enemiesBullets[:]:
            if b.rect.colliderect(player.rect):
                enemiesBullets.remove(b)
                pygame.time.set_timer(enemy_timer, 0) 
                pygame.time.set_timer(boss_timer, 0)
                return score
        
        # Colisão player -> inimigo
        for e in enemies[:]:
            if player.rect.colliderect(e.rect):
                pygame.time.set_timer(enemy_timer, 0) 
                pygame.time.set_timer(boss_timer, 0)
                return score

        # --- Desenho ---
        screen.fill((6, 8, 18))
        for s in stars:
            r = 1 if s[2] < 0.6 else (2 if s[2] < 1.0 else 3)
            pygame.draw.circle(screen, (200,200,255), (int(s[0]), int(s[1])), r)

        player.draw(screen)
        for e in enemies:
            e.draw(screen)
        for b in playerBullets:
            b.draw(screen)
        for b in enemiesBullets:
            b.draw(screen)

        display_hud(score)
        pygame.display.flip()
