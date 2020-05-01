import pygame

import constants
import utilities
from controls import Label
from listeners import MouseListener


class DialogBox(MouseListener):

    def __init__(self, orientation, position, dimensions, texts):
        self._texts = texts
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
        self._text_box = Label(padded_position, (720, 240), texts[0], font_size=40, multiline=True)

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
