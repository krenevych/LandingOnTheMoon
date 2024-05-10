from abc import ABCMeta, abstractmethod


class Node(metaclass=ABCMeta):
    def __init__(self, id):
        self.id = id

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass