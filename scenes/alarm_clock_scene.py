import constants
from controls import Button
from .scene import Scene


class AlarmClockScene(Scene):

    def __init__(self, scene_manager):
        super().__init__(scene_manager,
                         'background_images/alarmClockScene.png',
                         constants.ALARM_CLOCK_SCENE)
        self._skip_button = Button(
            constants.ALARM_CLOCK_SCENE_SKIP_BUTTON_TEXT,
            constants.MAIN_MENU_EXIT_BUTTON_COORDS,
            constants.MAIN_MENU_EXIT_BUTTON_DIMENSIONS
        )

    def handle_mouse_motion(self, coords):
        self._skip_button.handle_mouse_motion(coords)

    def handle_mouse_button_up(self, coords):
        if self._skip_button.handle_mouse_button_up():
            self._scene_manager.change_scene(constants.RESTAURANT_SCENE)

    def handle_mouse_button_down(self, coords):
        self._skip_button.handle_mouse_button_down()

    def draw(self, screen):
        super().draw(screen)
        self._skip_button.draw(screen)
