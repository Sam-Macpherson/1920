import constants
from controls import Button, DialogBox
from exceptions import TransitionScene
from .scene import Scene


class AlarmClockScene(Scene):

    def __init__(self):
        super().__init__('background_images/alarmClockScene.png',
                         constants.ALARM_CLOCK_SCENE)
        self._dialog_box = DialogBox(
            constants.DIALOG_BOX_ORIENTATION_RIGHT,
            constants.DIALOG_BOX_COORDS,
            constants.DIALOG_BOX_DIMENSIONS,
            ['AAAA gggg yyyy zzzz.dsafsdfasdfasdfasdfaasdf awayy too long for one line.',
             'Second line.',
             'Third.',
             'Go to work already you fruitcake.']
        )
        self._skip_button = Button(
            constants.ALARM_CLOCK_SCENE_SKIP_BUTTON_TEXT,
            constants.ALARM_CLOCK_SCENE_SKIP_BUTTON_COORDS,
            constants.ALARM_CLOCK_SCENE_SKIP_BUTTON_DIMENSIONS
        )

    def handle_key_down(self, key):
        self._dialog_box.handle_key_down(key)

    def handle_mouse_motion(self, coords):
        self._skip_button.handle_mouse_motion(coords)

    def handle_mouse_button_up(self, coords):
        if self._skip_button.handle_mouse_button_up(coords):
            raise TransitionScene

    def handle_mouse_button_down(self, coords):
        self._skip_button.handle_mouse_button_down(coords)

    def draw(self, screen):
        super().draw(screen)
        self._dialog_box.draw(screen)
        self._skip_button.draw(screen)
