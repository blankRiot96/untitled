import math

import pygame

from src.shared import Canvas, Events

from .input import check_keys
from .misc import Time


class WASDArrowController:
    """Basic WASD/Arrow keys controller for the player"""

    @staticmethod
    def get_wasd_arrow_input() -> pygame.Vector2:
        dx, dy = 0, 0
        if check_keys(Events.keys, [pygame.K_w, pygame.K_UP]):
            dy -= 1
        elif check_keys(Events.keys, [pygame.K_s, pygame.K_DOWN]):
            dy += 1

        if check_keys(Events.keys, [pygame.K_d, pygame.K_RIGHT]):
            dx += 1
        elif check_keys(Events.keys, [pygame.K_a, pygame.K_LEFT]):
            dx -= 1

        return pygame.Vector2(dx, dy)


class Pellet:
    """Basic pellet"""

    def __init__(self, image, position, radians, speed, distance=None) -> None:
        self.image = pygame.transform.rotate(image, -math.degrees(radians))
        self.position = pygame.Vector2(position)
        self.radians = radians
        self.speed = speed
        self.distance = distance

        self.dv = pygame.Vector2(math.cos(radians) * speed, math.sin(radians) * speed)
        self.rect = pygame.Rect(self.position, self.image.get_size())
        self.alive = True
        self.moved = 0.0

    def update(self):
        self.position += self.dv * Events.dt
        self.rect.topleft = self.position

        if self.distance is not None:
            self.moved += (self.dv * Events.dt).magnitude()
            if self.moved >= self.distance:
                self.alive = False

    def draw(self):
        Canvas.screen.blit(self.image, Canvas.camera.transform(self.rect))


class GenericGun:
    """Gun that handles shooting mechanism"""

    def __init__(
        self, pellet_image, pellet_speed, pellet_distance=None, cool_down=0.0
    ) -> None:
        self.pellet_image = pellet_image
        self.pellet_speed = pellet_speed
        self.pellet_distance = pellet_distance
        self.cool_down = Time(cool_down)
        self.pellets: list[Pellet] = []

    def add_pellet(self, radians: float, pos):
        if not self.cool_down.tick():
            return
        self.pellets.append(
            Pellet(
                self.pellet_image,
                pos,
                radians,
                self.pellet_speed,
                self.pellet_distance,
            )
        )

    def update(self):
        for pellet in self.pellets[:]:
            pellet.update()

            if not pellet.alive:
                self.pellets.remove(pellet)

    def draw(self):
        for pellet in self.pellets:
            pellet.draw()
