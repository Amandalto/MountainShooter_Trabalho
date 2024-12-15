from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.vertical_direction = 1  # 1 para descendo, -1 para subindo

    def move(self):
        # Movimento horizontal (igual para todos os inimigos)
        self.rect.centerx -= ENTITY_SPEED[self.name]

        if self.name == 'Enemy3':
            # Movimento vertical diferenciado
            if self.rect.top <= 0:  # Bate na borda superior
                self.vertical_direction = 1  # Começa a descer
                self.rect.centery += 2 * ENTITY_SPEED[self.name]  # Desce com o dobro da velocidade
            elif self.rect.bottom >= WIN_HEIGHT:  # Bate na borda inferior
                self.vertical_direction = -1  # Começa a subir
                self.rect.centery += self.vertical_direction * ENTITY_SPEED[self.name]
            else:
                # Movimento padrão de subida/descida
                self.rect.centery += self.vertical_direction * ENTITY_SPEED[self.name]
        else:
            # Outros inimigos se movem apenas na horizontal
            self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
