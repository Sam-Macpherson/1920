import pygame

from controls import Button
from .scene import Scene


class MainMenu(Scene):

    def __init__(self):
        self._exit_button = Button('Exit', (0, 0), (100, 50))
        super().__init__('background_images/mainMenu.png')

    def handle_mouse_motion(self, coords):
        print('main menu mouse motion', coords)

    def handle_mouse_button_up(self, coords):
        print('main menu mouse up', coords)

    def handle_mouse_button_down(self, coords):
        print('main menu mouse down', coords)


