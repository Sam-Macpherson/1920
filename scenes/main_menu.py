import constants
from controls import Button
from exceptions import Terminate
from .scene import Scene


class MainMenu(Scene):

    def __init__(self):
        self._exit_button = Button(
            constants.MAIN_MENU_EXIT_BUTTON_TEXT,
            constants.MAIN_MENU_EXIT_BUTTON_COORDS,
            constants.MAIN_MENU_EXIT_BUTTON_DIMENSIONS
        )
        self._settings_button = Button(
            constants.MAIN_MENU_SETTINGS_BUTTON_TEXT,
            constants.MAIN_MENU_SETTINGS_BUTTON_COORDS,
            constants.MAIN_MENU_SETTINGS_BUTTON_DIMENSIONS
        )
        self._buttons = [self._exit_button, self._settings_button]
        super().__init__('background_images/mainMenu.png')

    def handle_mouse_motion(self, coords):
        for button in self._buttons:
            button.handle_mouse_motion(coords)

    def handle_mouse_button_up(self, coords):
        if self._exit_button.handle_mouse_button_up():
            raise Terminate
        if self._settings_button.handle_mouse_button_up():
            print('Settings button clicked.')

    def handle_mouse_button_down(self, coords):
        for button in self._buttons:
            button.handle_mouse_button_down()

    def draw(self, screen):
        super().draw(screen)
        for button in self._buttons:
            button.draw(screen)
