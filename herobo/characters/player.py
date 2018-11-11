import pyxel
from characters.character import Character

class Player:
    def __init__(self):
        self.character = Character()

    def act(self):
        # self.character.position['x'] = (self.character.position['x'] + 1) % pyxel.width

        # GAMEPAD_1_LEFT throwing error.
        # if (pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.GAMEPAD_1_LEFT)) and (pyxel.btn(pyxel.KEY_F) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT)):
        #     self.character.momentum_horizontal = 0
        # elif pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.GAMEPAD_1_LEFT):
        #     self.character.momentum_horizontal = 1
        # elif pyxel.btn(pyxel.KEY_F) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
        #     self.character.momentum_horizontal = -1
        # else:
        #     self.character.momentum_horizontal = 0

        if pyxel.btn(pyxel.KEY_S) and pyxel.btn(pyxel.KEY_F):
            self.character.momentum_horizontal = 0
        elif pyxel.btn(pyxel.KEY_S):
            self.character.momentum_horizontal = -1
        elif pyxel.btn(pyxel.KEY_F):
            self.character.momentum_horizontal = 1
        else:
            self.character.momentum_horizontal = 0

        self.character.act()