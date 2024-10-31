import pygame

from .python import lru_cache


@lru_cache
def load_image(
    path: pygame.typing.FileLike, alpha: bool = False, scale: float = 1.0
) -> pygame.Surface:
    img = pygame.image.load(path)
    if scale != 1.0:
        img = pygame.transform.scale_by(img, scale)

    if alpha:
        return img.convert_alpha()

    return img.convert()
