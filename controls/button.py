from pygame.rect import Rect

import constants

from controls import Label


class Button:

    def __init__(self, text, position, dimensions):
        self._hovered = False
        self._mouse_downed = False
        self._label = Label(position, dimensions, text, font_size=dimensions[1] - constants.BUTTON_TEXT_PADDING)
        self._hit_box = Rect(position, dimensions)
        self._position = position
        self._dimensions = dimensions
        super().__init__()

    def handle_mouse_motion(self, coords):
        self._hovered = self._hit_box.collidepoint(coords)

    def handle_mouse_button_up(self):
        clicked = False

        if self._hovered and self._mouse_downed:
            clicked = True
        self._mouse_downed = False
        self._hovered = False
        return clicked

    def handle_mouse_button_down(self):
        if self._hovered:
            self._mouse_downed = True

    def draw(self, screen):
        if self._hovered:
            border = constants.GREY
            background = constants.WHITE
        else:
            border = constants.WHITE
            background = constants.GREY
        screen.fill(border, self._hit_box)
        screen.fill(background,
                    self._hit_box.inflate(-constants.BUTTON_BORDER_WEIGHT, -constants.BUTTON_BORDER_WEIGHT))
        self._label.draw(screen)
