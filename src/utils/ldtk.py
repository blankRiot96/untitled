import json
from pathlib import Path

import pygame
from pygame.typing import _PathLike

from src.shared import Canvas


class EntitySchema:
    def __init__(self, data: dict) -> None:
        self.id = data["id"]
        self.pos = pygame.Vector2(data["x"], data["y"]) * Canvas.entities_scale
        self.width = data["width"]
        self.height = data["height"]
        self.custom_fields = data["customFields"]


class LDTKMap:
    def __init__(self, map_folder_path: _PathLike, level_name: str) -> None:
        self.map_folder = Path(map_folder_path)
        self.level_folder = self.map_folder / "simplified" / level_name
        self.map_file = self.map_folder.parent / "map.ldtk"
        self.map_json_file = self.level_folder / "data.json"

        with open(self.map_json_file) as f:
            self.data = json.load(f)

        self.layers = [
            pygame.image.load(self.level_folder / layer).convert_alpha()
            for layer in self.data["layers"]
        ]
        self.layers = [
            pygame.transform.scale_by(layer, Canvas.entities_scale)
            for layer in self.layers
        ]

        self.entities = {
            entity_name: [EntitySchema(schema) for schema in data]
            for entity_name, data in self.data["entities"].items()
        }

        self.offset = (
            pygame.Vector2(self.data["x"], self.data["y"]) * Canvas.entities_scale
        )
