import pygame

from src.shared import Events

from .input import check_keys


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
