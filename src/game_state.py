from src.player import Player
from src.shared import Canvas, Entities, States


class GameState:
    def __init__(self) -> None:
        States.next_state = None
        Canvas.entities_scale = 3.5
        Entities.player = Player()

    def update(self):
        Entities.player.update()

    def draw(self):
        Entities.player.draw()
