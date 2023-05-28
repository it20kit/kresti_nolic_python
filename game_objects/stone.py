class Stone:
    """реализует крестик или нолик"""

    def __init__(self, color: str, index: int):
        self.__color = color
        self.__index = index

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index
