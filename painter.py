import sys
import pygame
from src.Palette import Palette

WIDTH: int = 800
HEIGHT: int = 600

class Painter:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Sprite Painter")
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

        self.canvas: pygame.surface.Surface = None 
        self.palette = Palette()

        self._resize()

    def run(self) -> None:
        while True:
            self.surface.blit(self.canvas, (0,0))
            self.canvas.fill((0,0,0))

            self.surface.blit(self.palette.surf, (self.canvas.get_width(), 0))
            self.palette.surf.fill((100,100,100))

            self.palette.draw_palette(self.canvas)
            print(self.palette.color_selected)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.WINDOWRESIZED:
                    self._resize()

            pygame.display.update()
            self.clock.tick(60)

    def _resize(self) -> None:
        self.canvas = pygame.surface.Surface((2 * self.surface.get_width() / 3, self.surface.get_height()))
        self.palette.resize(self.surface)

if __name__=='__main__':
    Painter().run()
