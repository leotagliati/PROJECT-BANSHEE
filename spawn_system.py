import random
from Entities.enemies import *
from game_config import HEIGHT, WIDTH

# --- Dicionário de inimigos possíveis ---
ENEMY_TYPES = [
    {"class": BasicEnemy, "cost": 1},
    {"class": ShooterEnemy, "cost": 2},
]
class SpawnSystem:
    def __init__(self, budget):
        self.budget = budget
    
    def spawn_enemy(self, x_spawn=WIDTH+10):
        """Retorna UM inimigo (ou None se não houver orçamento)."""
        # Filtra só os inimigos que cabem no orçamento
        print(self.budget)
        affordable = [e for e in ENEMY_TYPES if e["cost"] <= self.budget]
        if not affordable:
            return None  # não dá pra criar inimigos

        choice = random.choice(affordable)
        y = random.randint(10, HEIGHT - 20)
        enemy = choice["class"](x_spawn, y)
        self.budget -= choice["cost"]
        return enemy

    def spawn_boss(self, x_spawn=WIDTH-50):
        y = HEIGHT/2
        
        boss = MotherEnemy(x_spawn,y)
        
        return boss
    def add_budget(self,value):
        self.budget += value