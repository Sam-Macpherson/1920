import pygame

import constants
import utilities
from .scene import Scene


class RestaurantScene(Scene):

    def __init__(self, scene_manager):
        super().__init__(scene_manager,
                         'background_images/restaurantScene.png',
                         constants.RESTAURANT_SCENE)

    def handle_mouse_motion(self, coords):
        pass

    def handle_mouse_button_up(self, coords):
        pass

    def handle_mouse_button_down(self, coords):
        pass

    def draw(self, screen):
        super().draw(screen)
        sprite = pygame.image.load(utilities.relative_path('../sprites/defaultSprite.png', __file__))
        screen.blit(sprite, constants.ORIGIN)
