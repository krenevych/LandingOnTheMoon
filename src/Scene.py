from tkinter import Canvas


class Scene(Canvas):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self.nodes = [] # графічні елементи

    def addNode(self, node):
        self.nodes.append(node)

    def update(self):
        pass # пробігатися по всіх графічних елементах і оновлювати їхній стан

    def handleEvent(self, event):
        pass






