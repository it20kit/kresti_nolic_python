class Vector:
    """реализует храниние информации о размере полотна"""

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y
