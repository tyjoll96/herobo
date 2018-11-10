import pyxel
from characters.character import Character 

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        self.player = Character()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.act()

    def draw(self):
        pyxel.cls(0)
        self.player.render()

App()