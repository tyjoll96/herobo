import pyxel

class Character:
    def __init__(self):
        self.momentum_horizontal = 0
        self.position = {
            'x': 0,
            'y': 0
        }

    def act(self):
        self.position['x'] += self.momentum_horizontal

    def render(self):
        # pyxel.rect(self.position['x'], 0, self.position['x'] + 7, 7, 9)
        pyxel.blt(self.position['x'], self.position['y'], 0, 0, 0, 16, 16, 5)
        pyxel.text(0, 0, str(self.position['x']), 7)