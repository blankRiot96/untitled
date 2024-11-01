import pygame

from src.shared import Events
from src.utils import load_font


class Button:
    def __init__(
        self,
        text: str,
        topleft: pygame.typing.Point,
        size: tuple[int, int],
        bg_color: pygame.typing.ColorLike,
        fg_color: pygame.typing.ColorLike,
    ) -> None:
        self.image = pygame.Surface(size)
        self.image.fill(bg_color)
        self.rect = pygame.Rect(topleft, size)
        self.font = load_font("assets/fonts/maple.ttf", int(size[1] / 2))
        text_surf = self.font.render(text, True, fg_color)
        self.image.blit(text_surf, text_surf.get_rect(center=self.rect.center))

        self.is_hovering = False
        self.is_just_clicked = False

    def update(self):
        pass
