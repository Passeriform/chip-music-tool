import pygame
from .Tracker import Tracker
from .Roll import Roll
from .RollHandler import RollHandler

class Arrangement:
    def __init__(self, roll_handler: RollHandler) -> None:
        self.surf: pygame.surface.Surface = None

        self.tracker = Tracker(roll_handler)
        self.roll = Roll()

    def resize(self, parent_surf: pygame.surface.Surface) -> None:
        self.surf = pygame.surface.Surface((2 * parent_surf.get_width() // 3, parent_surf.get_height()))
        self.tracker.resize(self.surf)
        self.roll.resize(self.surf)

    def blit(self, parent_surf: pygame.surface.Surface, coordinates: tuple[int, int]) -> None:
        parent_surf.blit(self.surf, coordinates)

        self.tracker.blit(self.surf, (0,0))
        self.roll.blit(self.surf, (0, self.tracker.surf.get_height()))

    def set_color(self, color: str):
        self.tracker.color_selected = color
