import pygame

from controls import Button
from .scene import Scene


class MainMenu(Scene):

    def __init__(self):
        self._exit_button = Button('Exit', (0, 0), (100, 50))
        super().__init__('background_images/mainMenu.png')


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self._exit_button.is_hovered():

        elif event.type == pygame.MOUSEMOTION:
            if self._exit_button.is_hovered():


