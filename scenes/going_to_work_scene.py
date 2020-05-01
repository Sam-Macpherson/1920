import constants
from controls import Button
from exceptions import TransitionScene
from .scene import Scene


class GoingToWorkScene(Scene):

    def __init__(self):
        super().__init__('background_images/goingToWorkScene.png',
                         constants.GOING_TO_WORK_SCENE)
        self._skip_button = Button(
            constants.GOING_TO_WORK_SCENE_SKIP_BUTTON_TEXT,
            constants.MAIN_MENU_EXIT_BUTTON_COORDS,
            constants.MAIN_MENU_EXIT_BUTTON_DIMENSIONS
        )

    def handle_key_down(self, key):
        pass

    def handle_mouse_motion(self, coords):
        self._skip_button.handle_mouse_motion(coords)

    def handle_mouse_button_up(self, coords):
        if self._skip_button.handle_mouse_button_up(coords):
            raise TransitionScene

    def handle_mouse_button_down(self, coords):
        self._skip_button.handle_mouse_button_down(coords)

    def draw(self, screen):
        super().draw(screen)
        self._skip_button.draw(screen)
