import pygame
from pygame.rect import Rect

import constants


class Label:

    def __init__(self, position, dimensions, text, font_size=84, multiline=False):
        self._box = Rect(position, dimensions)
        self._text = text
        self._multiline = multiline
        self._rendered_text = constants.LEMON_MILK_REGULAR[font_size].render(self._text, fgcolor=constants.BLACK)[0]
        super().__init__()

    def draw(self, screen):
        text_box = self._rendered_text.get_rect(center=self._box.center)
        screen.blit(self._rendered_text, text_box)
