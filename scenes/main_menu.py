import constants
from controls import Button
from exceptions import Terminate
from .scene import Scene


class MainMenu(Scene):

    def __init__(self):
        self._exit_button = Button(constants.MAIN_MENU_EXIT_BUTTON_TEXT, (1437, 942), (415, 80))
        super().__init__('background_images/mainMenu.png')

    def handle_mouse_motion(self, coords):
        self._exit_button.handle_mouse_motion(coords)

    def handle_mouse_button_up(self, coords):
        if self._exit_button.handle_mouse_button_up():
            raise Terminate

    def handle_mouse_button_down(self, coords):
        self._exit_button.handle_mouse_button_down()

    def draw(self, screen):
        super().draw(screen)
        self._exit_button.draw(screen)
