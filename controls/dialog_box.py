import pygame
from pygame.constants import K_SPACE

import constants
import utilities
from controls import Label
from listeners import MouseListener, KeyListener


class DialogBox(MouseListener, KeyListener):

    def __init__(self, orientation, position, dimensions, dialog_tree, speaker_image):
        self._current_node = dialog_tree
        self._orientation = orientation
        self._position = position
        self._dimensions = dimensions
        self._speaker = pygame.image.load(utilities.relative_path(speaker_image, __file__))
        background_file = utilities.relative_path('control_assets/dialogBox.png', __file__)
        self._background = pygame.image.load(background_file)
        padded_position = (position[0] + constants.DIALOG_BOX_TEXT_PADDING,
                           position[1] + constants.DIALOG_BOX_TEXT_PADDING)
        self._text_box = Label(padded_position,
                               (constants.DIALOG_BOX_DIMENSIONS[0] * .75 - (2 * constants.DIALOG_BOX_TEXT_PADDING),
                                constants.DIALOG_BOX_DIMENSIONS[1] * .75 - (2 * constants.DIALOG_BOX_TEXT_PADDING)),
                               self._current_node.get_text(),
                               font_size=35,
                               multiline=True)

    def _next_string(self):
        self._current_node = self._current_node.follow_link(0)
        self._text_box.set_string(self._current_node.get_text())

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

    def _draw_speaker(self, screen):
        speaker_dimensions = (int(constants.DIALOG_BOX_DIMENSIONS[0] * .25),
                              int(constants.DIALOG_BOX_DIMENSIONS[0] * .25))
        self._speaker = pygame.transform.scale(self._speaker, speaker_dimensions)
        speaker_position = (constants.DIALOG_BOX_COORDS[0] + int(0.75 * constants.DIALOG_BOX_DIMENSIONS[0]),
                            constants.DIALOG_BOX_COORDS[1])
        screen.blit(self._speaker, speaker_position)

    def draw(self, screen):
        self._draw_background(screen)
        self._draw_speaker(screen)
        self._text_box.draw(screen)
