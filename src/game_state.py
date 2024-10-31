from src.player import Player
from src.shared import Entities, States


class GameState:
    def __init__(self) -> None:
        States.next_state = None
        Entities.player = Player()

    def update(self):
        Entities.player.update()

    def draw(self):
        Entities.player.draw()
