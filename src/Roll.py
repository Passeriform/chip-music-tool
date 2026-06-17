import pygame

class Roll:
    def __init__(self) -> None:
        self.surf: pygame.surface.Surface = None

    def resize(self, parent_surf: pygame.surface.Surface) -> None:
        self.surf = pygame.surface.Surface((parent_surf.get_width(), parent_surf.get_height() // 4))

    def blit(self, parent_surf: pygame.surface.Surface, coordinates: tuple[int, int]) -> None:
        parent_surf.blit(self.surf, coordinates)
        self.surf.fill((200,100,200))