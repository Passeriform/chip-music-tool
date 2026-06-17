import sys
import pygame

from src.Arrangement import Arrangement
from src.Scale import Scale
from src.RollHandler import RollHandler

WIDTH: int = 800
HEIGHT: int = 600

class Composer:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("ChipTune Composer")
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

        self.roll_handler = RollHandler()
        self.arrangement = Arrangement(self.roll_handler)
        self.scale = Scale()

        self._resize()

    def run(self) -> None:
        while True:
            self.arrangement.blit(self.surface, (0,0))
            self.scale.blit(self.surface, (self.arrangement.surf.get_width(), 0))

            self.arrangement.set_color(self.scale.get_color())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.WINDOWRESIZED:
                    self._resize()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.roll_handler.offset -= 128 * 8 if self.roll_handler.offset >= 128 * 8 else 0
                        self.arrangement.tracker.reset()
                    if event.key == pygame.K_DOWN:
                        self.roll_handler.offset += 128 * 8 if self.roll_handler.offset < (128 * 32) - 128 * 8 else 0
                        self.arrangement.tracker.reset()
                    if event.key == pygame.K_LEFT:
                        self.roll_handler.offset -= 8 if self.roll_handler.offset >= 8 else 0
                        self.arrangement.tracker.reset()
                    if event.key == pygame.K_RIGHT:
                        self.roll_handler.offset += 8 if self.roll_handler.offset < (128 * 32) - 8 else 0
                        self.arrangement.tracker.reset()
                    if event.key == pygame.K_s:
                        self.roll_handler.save("roll.csv")

            pygame.display.update()
            self.clock.tick(60)

    def _resize(self) -> None:
        self.arrangement.resize(self.surface)
        self.scale.resize(self.surface)

if __name__=='__main__':
    Composer().run()
