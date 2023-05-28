from painter.vector import Vector
from painter.canvas import Canvas
import os


class Painter:
    """реализует художника который может рисовть на полотне"""

    def __init__(self, width: int, height: int):
        self.canvas = Canvas(width, height)
        self.add_border("*")

    def add_picture(self, picture: str, x: int, y: int):
        """добавляет картинку на экрна по кординатам"""
        x -= 1
        y -= 1
        initial_x = x

        for i in range(len(picture)):
            if picture[i] == '\n':
                y += 1
                x = initial_x
                continue
            self.canvas.add(picture[i], Vector(x, y))
            x += 1

    def clear(self):
        """очищает полотно"""
        self.canvas.clear()
        self.add_border('*')
        os.system('clear')

    def add_border(self, symbol: str):
        """добавляет рамку на полотно"""
        size = self.canvas.get_size()
        width = size.x
        height = size.y

        for i in range(width):
            for j in range(height):
                if i == 0 or i == width - 1:
                    self.canvas.add(f'{symbol}', Vector(i, j))
                if j == 0 or j == height - 1:
                    self.canvas.add(f'{symbol}', Vector(i, j))

    def display(self):
        """воспроизводит полотно для игрока"""
        print(self.canvas.to_string())
