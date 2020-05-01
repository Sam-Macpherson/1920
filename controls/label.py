from pygame.rect import Rect
from pygame.surface import Surface

import constants


class Label:

    @staticmethod
    def _render_multiline(text, dimensions, font_size):
        text_surface = Surface(dimensions, constants.SRCALPHA)
        words = text.split(' ')
        font = constants.MONOFONTO[font_size]
        space = font.size(' ')[0]
        max_width, max_height = dimensions
        x, y = 0, 0
        for word in words:
            word_surface = font.render(word, True, constants.BLACK)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = 0  # Reset x to new line
                y += word_height  # Reset y to new line
            text_surface.blit(word_surface, (x, y))
            x += word_width + space
        return text_surface

    def __init__(self, position, dimensions, string, font_size=84, multiline=False):
        self._position = position
        self._dimensions = dimensions
        self._box = Rect(position, dimensions)
        self._string = string
        self._font_size = font_size
        self._multiline = multiline
        self._rendered_text = None
        self.set_string(string)
        super().__init__()

    def set_string(self, string):
        self._string = string
        if self._multiline:
            self._rendered_text = self._render_multiline(string, self._dimensions, self._font_size)
        else:
            self._rendered_text = constants.MONOFONTO[self._font_size].render(self._string, True, constants.BLACK)

    def draw(self, screen):
        text_box = self._rendered_text.get_rect(center=self._box.center)
        screen.blit(self._rendered_text, text_box)
