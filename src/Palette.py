import pygame

COLOR_PALETTE = [
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

class Palette:
    def __init__(self) -> None:
        self.surf: pygame.surface.Surface = None
        self.color_selected: str = None

        self._tile_size: float = 0 
        self._rects: list[pygame.rect.Rect] = []
        self._X_PADDING: float = 0 
        self._Y_PADDING: float = 0 

    def resize(self, parent_surf: pygame.surface.Surface) -> None:
        self.surf = pygame.surface.Surface((parent_surf.get_width() / 3, parent_surf.get_height()))
        self._tile_size = min(self.surf.get_width(), self.surf.get_height()) / 5
        self._define_color_rect()
        return self.surf

    def draw_palette(self, offset_surface: pygame.surface.Surface) -> None:
        for i in range(16):
            pygame.draw.rect(self.surf, pygame.Color(COLOR_PALETTE[i]), self._rects[i])
            self._hover_and_select(i, offset_surface)

    def _hover_and_select(self, idx: int, offset_surface: pygame.surface.Surface) -> None:
        transformed_mouse = (pygame.mouse.get_pos()[0] - offset_surface.get_width(), pygame.mouse.get_pos()[1] - 0)

        if self._rects[idx].collidepoint(transformed_mouse):
            pygame.draw.rect(self.surf, pygame.Color(0,0,0), self._rects[idx], 3)
            pygame.draw.rect(self.surf, pygame.Color(255,255,255), self._rects[idx], 2)
            pygame.draw.rect(self.surf, pygame.Color(0,0,0), self._rects[idx], 1)

            if pygame.mouse.get_pressed()[0]:
                self.color_selected = COLOR_PALETTE[idx]

    def _define_color_rect(self) -> None:
        self._rects: list[pygame.rect.Rect] = []
        self._X_PADDING = (self.surf.get_width() - (self._tile_size * 4)) / 2
        self._Y_PADDING = (self.surf.get_height() - (self._tile_size * 4)) / 2

        for i in range(16):
            x = (i % 4) * self._tile_size + self._X_PADDING
            y = (i // 4) * self._tile_size + self._Y_PADDING
            self._rects.append(pygame.rect.Rect(x, y, self._tile_size, self._tile_size))