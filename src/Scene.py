from tkinter import Canvas

from src.Ship import Ship


class Scene(Canvas):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.nodes = [] # графічні елементи

        self.ship = None

    def addNode(self, node):
        self.nodes.append(node)

    def update(self):
        # пробігатися по всіх графічних елементах і оновлювати їхній стан
        for node in self.nodes:
            node.update()

    def handleEvent(self, event):
        pass

    #################
    def addShip(self):
        ship = Ship(self, 50, 50)
        self.addNode(ship)
        self.ship = ship

    def setShipPosition(self, x, y):
        self.ship.setPosition(x, y)






