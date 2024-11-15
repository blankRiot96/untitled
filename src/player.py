import math

import pygame

from src import utils
from src.shared import Canvas, Events
from src.utils.ldtk import EntitySchema


class Player:
    SPEED = 100.0

    def __init__(self, schema: EntitySchema) -> None:
        self.schema = schema
        self.image = utils.load_image("assets/player.png", True, Canvas.entities_scale)
        self.rect = self.image.get_rect()
        self.pos = schema.pos
        self.dv = pygame.Vector2()

        self.gun = utils.GenericGun(
            utils.load_image("assets/pellet.png", True, Canvas.entities_scale),
            200,
            pellet_distance=1000,
            cool_down=0.1,
        )

    def check_input(self):
        self.dv = utils.WASDArrowController.get_wasd_arrow_input()
        if self.dv.length() != 0.0:
            self.dv.normalize_ip()

    def move(self):
        self.pos += self.dv * Player.SPEED * Events.dt

    def sync_positions(self):
        self.rect.topleft = self.pos

    def check_gun_shoot(self):
        if Events.mouse_press[0]:
            screen_pos = Canvas.camera.transform(self.pos)
            self.gun.add_pellet(
                math.atan2(
                    Events.mouse_pos.y - screen_pos.y, Events.mouse_pos.x - screen_pos.x
                ),
                self.rect.center,
            )

    def update(self):
        self.check_input()
        self.move()
        self.sync_positions()
        self.check_gun_shoot()
        self.gun.update()

    def draw(self):
        self.gun.draw()
        Canvas.screen.blit(self.image, Canvas.camera.transform(self.rect))
