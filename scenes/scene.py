from abc import ABC

import pygame

import constants
import utilities
from listeners import MouseListener, KeyListener


class Scene(MouseListener, KeyListener, ABC):

    def __init__(self, background, constant):
        self._constant = constant

        if isinstance(background, str):
            utilities.relative_path(background)
            self._background = pygame.image.load(utilities.relative_path(background, __file__))
        else:
            self._background = background
        super().__init__()

    def _draw_background(self, screen):
        if isinstance(self._background, pygame.Surface):
            self._background = pygame.transform.scale(self._background, screen.get_size())
            screen.blit(self._background, constants.ORIGIN)
        elif isinstance(self._background, tuple):
            screen.fill(self._background)

    def constant(self):
        return self._constant

    def draw(self, screen):
        self._draw_background(screen)
