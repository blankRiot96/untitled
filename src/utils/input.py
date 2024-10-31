import typing as t

import pygame


def check_keys(keys: pygame.key.ScancodeWrapper, key_values: t.Sequence[int]):
    return any(keys[key] for key in key_values)
