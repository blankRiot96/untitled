import pygame

from src import utils
from src.shared import Canvas, Entities, Events


class Enemy:
    SPEED = 20.0
    STOPPING_DISTANCE = 200.0

    def __init__(self, center) -> None:
        self.image = utils.load_image("assets/enemy.png", True, Canvas.entities_scale)
        self.rect = self.image.get_rect(center=center)
        self.center = pygame.Vector2(center)
        self.tracker = utils.Tracker(self.center, Enemy.SPEED, Enemy.STOPPING_DISTANCE)
        self.center = self.tracker.pos

    def update(self):
        self.tracker.update(Entities.player.pos)
        self.rect.center = self.center

    def draw(self):
        Canvas.screen.blit(self.image, Canvas.camera.transform(self.center))


class EnemySpawner:
    def __init__(self, schema: utils.EntitySchema) -> None:
        self.image = utils.load_image(
            "assets/enemy_spawner.png", True, Canvas.entities_scale
        )
        self.rect = self.image.get_rect(topleft=schema.pos)
        self.enemies: list[Enemy] = []
        self.cool_down = utils.Time(1.5)

    def update(self):
        if self.cool_down.tick():
            self.enemies.append(Enemy(self.rect.center))

        for enemy in self.enemies:
            enemy.update()

    def draw(self):
        Canvas.screen.blit(self.image, Canvas.camera.transform(self.rect))
        for enemy in self.enemies:
            enemy.draw()
