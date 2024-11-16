import math
import random

import pygame

from src import utils
from src.shared import Canvas, Entities, Events


class Enemy:
    SPEED = 20.0
    STOPPING_DISTANCE = 200.0
    MIN_PIXELS_BETWEEN_OTHER = 30.0

    def __init__(self, center) -> None:
        self.original_image = utils.load_image(
            "assets/enemy.png", True, Canvas.entities_scale
        )
        self.original_rect = self.original_image.get_rect(center=center)

        self.image = self.original_image.copy()
        self.rect = self.original_rect.copy()
        self.center = pygame.Vector2(center)
        self.tracker = utils.Tracker(self.center, Enemy.SPEED, Enemy.STOPPING_DISTANCE)
        self.center = self.tracker.pos
        self.radians = 0.0
        self.random_radian_target = random.uniform(0, math.pi * 2)
        self.image_rotated_radians_vec = pygame.Vector2(0.0, 0.0)

    def update(self):
        self.tracker.update(Entities.player.pos)
        self.rect.center = self.center
        self.radians = math.atan2(
            self.center.y - Entities.player.pos.y, self.center.x - Entities.player.pos.x
        )

        self.image_rotated_radians_vec.move_towards_ip(
            (self.random_radian_target, 0), 1 * Events.dt
        )
        if self.image_rotated_radians_vec.x == self.random_radian_target:
            self.random_radian_target = random.uniform(0, math.pi * 2)
        self.image = pygame.transform.rotate(
            self.original_image, math.degrees(self.image_rotated_radians_vec.x)
        )

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

            for enemy_2 in self.enemies:
                if enemy_2 is enemy:
                    continue
                dist = enemy.center.distance_to(enemy_2.center)
                if dist < Enemy.MIN_PIXELS_BETWEEN_OTHER:
                    val = Enemy.MIN_PIXELS_BETWEEN_OTHER - dist
                    angle = enemy.radians + (math.pi / 2)
                    enemy.center.x += math.cos(angle) * val
                    enemy.center.y += math.sin(-angle) * val
                    enemy.rect.center = enemy.center

    def draw(self):
        Canvas.screen.blit(self.image, Canvas.camera.transform(self.rect))
        for enemy in self.enemies:
            enemy.draw()
