import constants
from controls import Button
from exceptions import TransitionScene
from .scene import Scene


class AlarmClockScene(Scene):

    def __init__(self):
        super().__init__('background_images/alarmClockScene.png',
                         constants.ALARM_CLOCK_SCENE)
        self._skip_button = Button(
            constants.ALARM_CLOCK_SCENE_SKIP_BUTTON_TEXT,
            constants.ALARM_CLOCK_SCENE_SKIP_BUTTON_COORDS,
            constants.ALARM_CLOCK_SCENE_SKIP_BUTTON_DIMENSIONS
        )

    def handle_mouse_motion(self, coords):
        self._skip_button.handle_mouse_motion(coords)

    def handle_mouse_button_up(self, coords):
        if self._skip_button.handle_mouse_button_up():
            raise TransitionScene

    def handle_mouse_button_down(self, coords):
        self._skip_button.handle_mouse_button_down()

    def draw(self, screen):
        super().draw(screen)
        self._skip_button.draw(screen)
