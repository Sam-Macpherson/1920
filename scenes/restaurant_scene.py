import pygame

import constants
import utilities
from controls import Button
from exceptions import TransitionScene
from .scene import Scene


class RestaurantScene(Scene):

    def __init__(self):
        super().__init__('background_images/restaurantScene.png',
                         constants.RESTAURANT_SCENE)
        self._close_restaurant_button = Button(
            constants.CLOSE_RESTAURANT_BUTTON_TEXT,
            constants.RESTAURANT_SCENE_CLOSE_BUTTON_COORDS,
            constants.RESTAURANT_SCENE_CLOSE_BUTTON_DIMENSIONS
        )

    def handle_mouse_motion(self, coords):
        self._close_restaurant_button.handle_mouse_motion(coords)

    def handle_mouse_button_up(self, coords):
        if self._close_restaurant_button.handle_mouse_button_up(coords):
            raise TransitionScene

    def handle_mouse_button_down(self, coords):
        self._close_restaurant_button.handle_mouse_button_down(coords)

    def draw(self, screen):
        super().draw(screen)
        # TODO
        sprite = pygame.image.load(utilities.relative_path('../sprites/defaultSprite.png', __file__))
        screen.blit(sprite, constants.ORIGIN)
        self._close_restaurant_button.draw(screen)
