import pygame

NOTES = ["C", "D", "E", "F", "G", "A", "B"]
OCTAVES = [3, 4, 5, 6]


class Scale:
    def __init__(self) -> None:
        self.surf: pygame.surface.Surface = None
        self.note_selected: str = None
        self.octave_selected: str = None
        self.modifier_toggled: bool = False

        self._tile_size: int = 0 
        self._rects: list[pygame.rect.Rect] = []
        self._X_PADDING: int = 0 
        self._Y_PADDING: int = 0 

    def resize(self, parent_surf: pygame.surface.Surface) -> None:
        self.surf = pygame.surface.Surface((parent_surf.get_width() // 3, parent_surf.get_height()))
        self._tile_size = min(self.surf.get_width(), self.surf.get_height()) // 5
        self.note_selected = self.note_selected or NOTES[0]
        self.octave_selected = self.octave_selected or OCTAVES[0]
        self.modifier_toggled = self.modifier_toggled or False
        self._rects = []
        self._define_scale_rects()
        return self.surf

    def get_note(self) -> str:
        return self.note_selected

    def blit(self, parent_surf: pygame.surface.Surface, coordinates: tuple[int, int]) -> None:
        parent_surf.blit(self.surf, coordinates)
        self.surf.fill((100,100,100))
        self._draw_scale(coordinates)

    def _draw_scale(self, offset: tuple[int, int]) -> None:
        for i in range(12):
            pygame.draw.rect(self.surf, pygame.Color("#1E1E1E"), self._rects[i])
            self._hover_and_select(i, offset)

    def _hover_and_select(self, idx: int, offset: tuple[int, int]) -> None:
        transformed_mouse = (pygame.mouse.get_pos()[0] - offset[0], pygame.mouse.get_pos()[1] - offset[1])

        if self._rects[idx].collidepoint(transformed_mouse):
            pygame.draw.rect(self.surf, pygame.Color(0,0,0), self._rects[idx], 3)
            pygame.draw.rect(self.surf, pygame.Color(255,255,255), self._rects[idx], 2)
            pygame.draw.rect(self.surf, pygame.Color(0,0,0), self._rects[idx], 1)

            if pygame.mouse.get_pressed()[0]:
                self.note_selected = NOTES[idx]

    def _define_scale_rects(self) -> None:
        self._X_PADDING = (self.surf.get_width() - (self._tile_size * 4)) // 2
        self._Y_PADDING = self.surf.get_height() - (self._tile_size * 4)

        x = self._tile_size + self._X_PADDING
        y = self._tile_size + self._Y_PADDING // 3
        self._rects.append(pygame.rect.Rect(x, y, self._tile_size, self._tile_size))

        for i in range(7):
            x = (i % 4) * self._tile_size + self._X_PADDING
            y = (i // 4) * self._tile_size + 2 * self._Y_PADDING // 3
            self._rects.append(pygame.rect.Rect(x, y, self._tile_size, self._tile_size))

        for i in range(4):
            x = (i % 4) * self._tile_size + self._X_PADDING
            y = 3 * (i // 4) * self._tile_size + self._Y_PADDING
            self._rects.append(pygame.rect.Rect(x, y, self._tile_size, self._tile_size))
