import typing as t

from src import shared
from src.enums import State
from src.game_state import GameState


class StateLike(t.Protocol):
    def update(self): ...

    def draw(self): ...


class StateManager:
    def __init__(self) -> None:
        self.state_dict: dict[State, type[StateLike]] = {
            State.GAME: GameState,
        }

        shared.next_state = State.GAME
        self.create_state_object()

    def create_state_object(self):
        assert shared.next_state
        state_cls = self.state_dict[shared.next_state]

        self.state_obj = state_cls()

    def update(self):
        self.state_obj.update()
        if shared.next_state is not None:
            self.create_state_object()

    def draw(self):
        self.state_obj.draw()
