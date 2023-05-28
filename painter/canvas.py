from painter.vector import Vector


class Canvas:
    """Реализует полотно которое хранит в себе информацию, и медоты для взаимодействия с ним"""

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.canvas = []
        self.init()

    def init(self):
        """создание пустого полотна, удаление старого"""
        self.canvas = []
        for i in range(self.height):
            line = []
            for j in range(self.width):
                line.append(' ')
            self.canvas.append(line)

    def get_size(self):
        """возвращает размер полотна"""
        return Vector(self.width, self.height)

    def add(self, symbol: str,  vector: Vector):
        """добавляет символ на полотно"""
        x = vector.x
        y = vector.y
        del self.canvas[y][x]
        self.canvas[y].insert(x, symbol)

    def clear(self):
        """очищает полотно"""
        self.init()

    def to_string(self):
        """отдает строковое представление полотна"""
        picture = ''
        for line in self.canvas:
            for symbol in line:
                picture += symbol
            picture += '\n'
        return picture
