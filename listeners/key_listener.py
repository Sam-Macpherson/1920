from abc import ABC


class KeyListener(ABC):

    def handle_key_down(self, key):
        raise NotImplementedError
