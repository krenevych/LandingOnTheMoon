from src.Node import Node


class Ship(Node):

    def __init__(self, canvas, x1, y1):
        id = canvas.create_rectangle(0, 0, x1, y1)
        self.scene = canvas
        super().__init__(id)

    def setPosition(self, x, y):
        self.pos = (x, y)

    def update(self):
        self.scene.moveto(self.id, self.pos[0], self.pos[1])

    def draw(self):
        pass



