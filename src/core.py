import pygame

from src.shared import Canvas, Events
from src.states import StateManager


class Core:
    def __init__(self) -> None:
        self.win_init()
        self.state_manager = StateManager()

    def win_init(self):
        pygame.display.set_caption("Untitled Game")
        pygame.init()
        Canvas.screen = pygame.display.set_mode((1100, 650))
        Canvas.screen_rect = Canvas.screen.get_rect()
        Events.clock = pygame.Clock()

    def get_events(self):
        Events.events = pygame.event.get()
        Events.dt = Events.clock.tick(60) / 1000
        Events.dt = max(Events.dt, 0.1)
        Events.keys = pygame.key.get_pressed()
        Events.keys_just_pressed = pygame.key.get_just_pressed()
        Events.keys_just_released = pygame.key.get_just_released()
        Events.mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        Events.mouse_press = pygame.mouse.get_pressed()

    def check_for_exit(self):
        for event in Events.events:
            if event.type == pygame.QUIT:
                raise SystemExit

    def update(self):
        self.get_events()
        self.check_for_exit()
        self.state_manager.update()

    def draw(self):
        Canvas.screen.fill("black")
        self.state_manager.draw()
        pygame.display.flip()

    def run(self):
        while True:
            self.update()
            self.draw()


def main():
    core = Core()
    core.run()
