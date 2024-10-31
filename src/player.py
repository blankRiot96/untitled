import pygame

from src import utils
from src.shared import Canvas, Events


class Player:
    SPEED = 100.0

    def __init__(self) -> None:
        self.image = utils.load_image("assets/player.png", True)
        self.rect = self.image.get_rect()
        self.pos = pygame.Vector2()
        self.dv = pygame.Vector2()

    def check_controls(self):
        dx, dy = 0, 0
        if utils.check_keys(Events.keys, [pygame.K_w, pygame.K_UP]):
            dy -= 1
        elif utils.check_keys(Events.keys, [pygame.K_s, pygame.K_DOWN]):
            dy += 1

        if utils.check_keys(Events.keys, [pygame.K_d, pygame.K_RIGHT]):
            dx += 1
        elif utils.check_keys(Events.keys, [pygame.K_a, pygame.K_LEFT]):
            dx -= 1

        self.dv = pygame.Vector2(dx, dy)
        if self.dv.length() != 0.0:
            self.dv.normalize_ip()

    def move(self):
        self.pos += self.dv * Player.SPEED * Events.dt

    def sync_positions(self):
        self.rect.topleft = self.pos

    def update(self):
        self.check_controls()
        self.move()
        self.sync_positions()

    def draw(self):
        Canvas.screen.blit(self.image, self.rect)
