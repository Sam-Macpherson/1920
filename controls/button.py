

class Button:

    def __init__(self, text, position, dimensions):
        self._text = text
        self._position = position
        self._dimensions = dimensions
        super().__init__()

    def is_hovered(self, position):
        return (self._position[0] <= position[0] <= self._position[0] + self._dimensions[0]) and \
               (self._position[1] <= position[1] <= self._position[1] + self._dimension[1])

    def draw(self, screen):
        pass
