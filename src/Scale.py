import pygame

NOTES = [
    "#000000",
    "#1D2B53",
    "#7E2553",
    "#008751",
    "#AB5236",
    "#5F574F",
    "#C2C3C7",
    "#FFF1E8",
    "#FF004D",
    "#FFA300",
    "#FFEC27",
    "#00E436",
    "#29ADFF",
    "#83769C",
    "#FF77A8",
    "#FFCCAA",
]

class Scale:
    def __init__(self) -> None:
        self.surf: pygame.surface.Surface = None
        self.color_selected: str = None

        self._tile_size: int = 0 
        self._rects: list[pygame.rect.Rect] = []
        self._X_PADDING: int = 0 
        self._Y_PADDING: int = 0 

    def resize(self, parent_surf: pygame.surface.Surface) -> None:
        self.surf = pygame.surface.Surface((parent_surf.get_width() // 3, parent_surf.get_height()))
        self._tile_size = min(self.surf.get_width(), self.surf.get_height()) // 5
        self.color_selected = self.color_selected or "#000000"
        self._define_color_rects()
        return self.surf

    def get_color(self) -> str:
        return self.color_selected

    def blit(self, parent_surf: pygame.surface.Surface, coordinates: tuple[int, int]) -> None:
        parent_surf.blit(self.surf, coordinates)
        self.surf.fill((100,100,100))
        self._draw_scale(coordinates)

    def _draw_scale(self, offset: tuple[int, int]) -> None:
        for i in range(16):
            pygame.draw.rect(self.surf, pygame.Color(NOTES[i]), self._rects[i])
            self._hover_and_select(i, offset)

    def _hover_and_select(self, idx: int, offset: tuple[int, int]) -> None:
        transformed_mouse = (pygame.mouse.get_pos()[0] - offset[0], pygame.mouse.get_pos()[1] - offset[1])

        if self._rects[idx].collidepoint(transformed_mouse):
            pygame.draw.rect(self.surf, pygame.Color(0,0,0), self._rects[idx], 3)
            pygame.draw.rect(self.surf, pygame.Color(255,255,255), self._rects[idx], 2)
            pygame.draw.rect(self.surf, pygame.Color(0,0,0), self._rects[idx], 1)

            if pygame.mouse.get_pressed()[0]:
                self.color_selected = NOTES[idx]

    def _define_color_rects(self) -> None:
        self._rects = []
        self._X_PADDING = (self.surf.get_width() - (self._tile_size * 4)) // 2
        self._Y_PADDING = (self.surf.get_height() - (self._tile_size * 4)) // 2

        for i in range(16):
            x = (i % 4) * self._tile_size + self._X_PADDING
            y = (i // 4) * self._tile_size + self._Y_PADDING
            self._rects.append(pygame.rect.Rect(x, y, self._tile_size, self._tile_size))