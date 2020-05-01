from abc import ABC


class MouseListener(ABC):

    def handle_mouse_motion(self, coords):
        raise NotImplementedError

    def handle_mouse_button_up(self, coords):
        raise NotImplementedError

    def handle_mouse_button_down(self, coords):
        raise NotImplementedError
