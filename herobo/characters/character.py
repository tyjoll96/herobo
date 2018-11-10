import pyxel

class Character:
    def __init__(self):
        self.position = {
            'x': 0,
            'y': 0
        }

    def act(self):
        self.position['x'] = (self.position['x'] + 1) % pyxel.width

    def render(self):
        pyxel.rect(self.position['x'], 0, self.position['x'] + 7, 7, 9)