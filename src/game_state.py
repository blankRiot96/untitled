from src.enemy import EnemySpawner
from src.player import Player
from src.shared import Canvas, Entities, States
from src.utils import Camera, LDTKMap


class GameState:
    def __init__(self) -> None:
        States.next_state = None
        Canvas.entities_scale = 3.5
        self.ldtk_map = LDTKMap("assets/map", "Level_0")
        Entities.player = Player(self.ldtk_map.entities["Player"][0])
        Entities.enemy_spawners = []
        for enemy_spawner_schema in self.ldtk_map.entities["EnemySpawner"]:
            Entities.enemy_spawners.append(EnemySpawner(enemy_spawner_schema))

        Canvas.camera = Camera()
        Canvas.camera.offset = Entities.player.pos.copy()

    def update(self):
        Canvas.camera.attach_to(Entities.player.pos)
        Entities.player.update()
        for spawner in Entities.enemy_spawners:
            spawner.update()

    def draw(self):
        for layer in self.ldtk_map.layers:
            Canvas.screen.blit(layer, Canvas.camera.transform((0, 0)))
        Entities.player.draw()
        for spawner in Entities.enemy_spawners:
            spawner.draw()
