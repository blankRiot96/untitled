from __future__ import annotations

import typing as t

import pygame

if t.TYPE_CHECKING:
    from src.enemy import EnemySpawner
    from src.enums import State
    from src.player import Player
    from src.utils.camera import Camera


class Entities:
    player: Player
    enemy_spawners: list[EnemySpawner]


class Canvas:
    entities_scale: float

    screen: pygame.Surface
    screen_rect: pygame.Rect
    camera: Camera


class Events:
    events: list[pygame.event.Event]
    mouse_pos: pygame.Vector2
    mouse_press: tuple[int, ...]
    keys: pygame.key.ScancodeWrapper
    keys_just_pressed: pygame.key.ScancodeWrapper
    keys_just_released: pygame.key.ScancodeWrapper
    dt: float
    clock: pygame.Clock


class States:
    next_state: State | None
