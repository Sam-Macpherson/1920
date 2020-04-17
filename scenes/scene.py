import os

import pygame


class Scene:

    def __init__(self, background):

        if isinstance(background, str):
            base_path = os.path.dirname(__file__)
            background_path = os.path.join(base_path, background)
            self._background = pygame.image.load(background_path)
        else:
            self._background = background
        super().__init__()

    def _draw_background(self, screen):
        if isinstance(self._background, pygame.Surface):
            self._background = pygame.transform.scale(self._background, screen.get_size())
            screen.blit(self._background, (0, 0))
        elif isinstance(self._background, tuple):
            screen.fill(self._background)

    def handle_event(self, event):
        raise NotImplementedError

    def draw(self, screen):
        self._draw_background(screen)
