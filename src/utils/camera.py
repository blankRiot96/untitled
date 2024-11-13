import typing as t

import pygame

from src.shared import Canvas


class Camera:
    def __init__(self) -> None:
        self.offset = pygame.Vector2()

    def attach_to(self, pos: t.Sequence):
        self.offset.x += (
            pos[0] - self.offset.x - (Canvas.screen_rect.width // 2)
        ) * 0.08
        self.offset.y += (
            pos[1] - self.offset.y - (Canvas.screen_rect.height // 2)
        ) * 0.08

    def transform(self, pos: t.Sequence) -> pygame.Vector2:
        return pygame.Vector2(pos[0] - self.offset.x, pos[1] - self.offset.y)
