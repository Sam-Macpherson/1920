from pygame.rect import Rect

import constants


class Button:

    def __init__(self, text, position, dimensions):
        self._text = text
        self._hit_box = Rect(position, dimensions)
        self._position = position
        self._dimensions = dimensions
        super().__init__()

    def is_hovered(self, position):
        return self._hit_box.collidepoint(position)

    def draw(self, screen):
        screen.fill(constants.GREY, self._hit_box)
        constants.BASKERVILLE_OLD_FACE_36.render_to(screen, self._position, self._text, constants.BLACK)
