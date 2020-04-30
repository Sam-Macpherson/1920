from pygame.rect import Rect
from pygame.surface import Surface

import constants


class Label:

    @staticmethod
    def _render_multiline(text, dimensions, font_size):
        text_surface = Surface(dimensions)  # , constants.SRCALPHA)
        words = text.split(' ')
        font = constants.LEMON_MILK_REGULAR[font_size]
        space = font.get_metrics(' ', font_size)[0][4]
        max_width, max_height = dimensions
        x, y = 0, 0
        for word in words:
            word_surface = font.render(word, fgcolor=constants.WHITE)[0]
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = 0  # Reset x to new line
                y += word_height  # Reset y to new line
            text_surface.blit(word_surface, (x, y))
            x += word_width + space
        return text_surface

    def __init__(self, position, dimensions, text, font_size=84, multiline=False):
        self._box = Rect(position, dimensions)
        self._text = text
        self._multiline = multiline
        if multiline:
            self._rendered_text = self._render_multiline(text, dimensions, font_size)
        else:
            self._rendered_text = constants.LEMON_MILK_REGULAR[font_size].render(self._text, fgcolor=constants.BLACK)[0]
        super().__init__()

    def draw(self, screen):
        text_box = self._rendered_text.get_rect(center=self._box.center)
        screen.blit(self._rendered_text, text_box)
