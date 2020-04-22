import constants
from scenes import MainMenuScene, RestaurantScene


class SceneFactory:

    @staticmethod
    def create_new_scene(scene, scene_manager):
        if scene == constants.MAIN_MENU_SCENE:
            new_scene = MainMenuScene(scene_manager)
        elif scene == constants.RESTAURANT_SCENE:
            new_scene = RestaurantScene(scene_manager)
        else:
            new_scene = None
        return new_scene


class SceneManager:

    def __init__(self):
        self._scene_history = []  # A stack of scenes
        self._current_scene_index = -1  # -1 indicates there are 0 scenes.
        super().__init__()

    def _push_scene_to_history(self, scene):
        self._scene_history.append(scene)
        self._current_scene_index += 1

    def _scene_at(self, index):
        if self._scene_history and len(self._scene_history) > index:
            return self._scene_history[index]
        return None

    def pop_scene(self):
        self._current_scene_index -= 1

    def change_scene(self, new_scene):
        # Overwrite the forward history if scenes have been popped.
        # Scene popping works like a browser's back button.
        if self._current_scene_index != len(self._scene_history) - 1 and \
                new_scene == self._scene_at(self._current_scene_index + 1).constant():
            self._current_scene_index += 1
            print('Not creating new scene', new_scene)
        else:
            print('Creating new scene', new_scene)
            del self._scene_history[self._current_scene_index + 1:]
            scene = SceneFactory.create_new_scene(new_scene, self)
            self._push_scene_to_history(scene)

    def current_scene(self):
        if self._current_scene_index == -1:
            return None
        else:
            return self._scene_history[self._current_scene_index]

    def handle_mouse_motion(self, coords):
        self.current_scene().handle_mouse_motion(coords)

    def handle_mouse_button_up(self, coords):
        self.current_scene().handle_mouse_button_up(coords)

    def handle_mouse_button_down(self, coords):
        self.current_scene().handle_mouse_button_down(coords)

    def draw_scene(self, screen):
        self.current_scene().draw(screen)
