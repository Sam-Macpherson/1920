import pygame
from pygame.constants import K_SPACE

import constants
import utilities
from controls import Label
from listeners import MouseListener, KeyListener


class DialogBox(MouseListener, KeyListener):

    def __init__(self, orientation, position, dimensions, texts):
        self._strings = texts
        self._current_string = 0
        self._orientation = orientation
        self._position = position
        self._dimensions = dimensions

        if orientation == constants.DIALOG_BOX_ORIENTATION_RIGHT:
            background_file = utilities.relative_path('control_assets/dialogBoxPictureRight.png', __file__)
        else:
            background_file = utilities.relative_path('control_assets/dialogBoxPictureLeft.png', __file__)
        self._background = pygame.image.load(background_file)
        # TODO Fix these dastardly magic numbers.
        padded_position = position[0] + 10, position[1] + 10
        self._text_box = Label(padded_position,
                               (720, 240),
                               self._strings[self._current_string],
                               font_size=40,
                               multiline=True)

    def _next_string(self):
        if self._current_string < len(self._strings) - 1:
            self._current_string += 1
            self._text_box.set_string(self._strings[self._current_string])

    def handle_key_down(self, key):
        if key == K_SPACE:
            self._next_string()

    def handle_mouse_motion(self, coords):
        pass

    def handle_mouse_button_up(self, coords):
        pass

    def handle_mouse_button_down(self, coords):
        pass

    def _draw_background(self, screen):
        self._background = pygame.transform.scale(self._background, self._dimensions)
        screen.blit(self._background, self._position)

    def draw(self, screen):
        self._draw_background(screen)
        self._text_box.draw(screen)
