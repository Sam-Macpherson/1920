import constants
from scenes.main_menu import MainMenu


class SceneFactory:

    @staticmethod
    def create_new_scene(scene):
        if scene == constants.MAIN_MENU:
            new_scene = MainMenu()
        else:
            new_scene = None
        return new_scene


class SceneManager:

    def __init__(self):
        self._scene_history = []  # A stack of scenes
        self._current_scene = None
        super().__init__()

    def _push_scene_to_history(self):
        self._scene_history.append(self._current_scene)

    def change_scene(self, new_scene):
        scene = SceneFactory.create_new_scene(new_scene)
        self._current_scene = scene
        self._push_scene_to_history()

    def current_scene(self):
        return self._current_scene

    def handle_mouse_motion(self, coords):
        self._current_scene.handle_mouse_motion(coords)

    def handle_mouse_button_up(self, coords):
        self._current_scene.handle_mouse_button_up(coords)

    def handle_mouse_button_down(self, coords):
        self._current_scene.handle_mouse_button_down(coords)

    def draw_scene(self, screen):
        self._current_scene.draw(screen)
