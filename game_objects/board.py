from game_objects.stone import Stone


class Board:
    """реализует игровую доску"""

    def __init__(self):
        self.storage = []

    def add_stone_stone_board(self, stone: Stone):
        """добовляет камень на доску"""
        self.storage.append(stone)

    def to_string(self,):
        """отдает строковое представление доски"""
        cell_index = 1
        number_of_cells_in_row = 0
        picture = ""
        total_cells_on_board = 9
        for i in range(total_cells_on_board):
            if self.is_there_such_stone_on_board_according_to_index(cell_index):
                stone = self.get_stone_by_index(cell_index)
                picture += f"[{stone.color}]"
            else:
                picture += "[ ]"
            cell_index += 1
            number_of_cells_in_row += 1
            if number_of_cells_in_row == 3:
                picture += '\n'
                number_of_cells_in_row = 0
        return picture

    def is_win(self, color: str):
        """проверяет стоят ли камни в победном положении"""
        def winning_rows(stone_color: str):
            """все цвета камней в ряду одинаковые?"""
            matches_in_first_row = 0
            matches_in_second_row = 0
            matches_in_third_row = 0
            matches_to_win = 3

            for stone in self.storage:
                if stone.color == stone_color:
                    if stone.index == 1 or stone.index == 2 or stone.index == 3:
                        matches_in_first_row += 1
                    if stone.index == 4 or stone.index == 5 or stone.index == 6:
                        matches_in_second_row += 1
                    if stone.index == 7 or stone.index == 8 or stone.index == 9:
                        matches_in_third_row += 1

            if matches_in_first_row == matches_to_win \
                    or matches_in_second_row == matches_to_win\
                    or matches_in_third_row == matches_to_win:
                return True
            return False

        def winning_column(stone_color: str):
            """все цвета камней в столбце одинаковые?"""
            matches_in_the_first_column = 0
            matches_in_the_second_column = 0
            matches_in_the_third_column = 0
            matches_to_win = 3

            for stone in self.storage:
                if stone.color == stone_color:
                    if stone.index == 1 or stone.index == 4 or stone.index == 7:
                        matches_in_the_first_column += 1
                    if stone.index == 2 or stone.index == 5 or stone.index == 8:
                        matches_in_the_second_column += 1
                    if stone.index == 3 or stone.index == 6 or stone.index == 9:
                        matches_in_the_third_column += 1

            if \
                    matches_in_the_first_column == matches_to_win \
                    or matches_in_the_second_column == matches_to_win \
                    or matches_in_the_third_column == matches_to_win:
                return True
            return False

        def victory_in_horizontal(stone_color: str):
            """все цвета камней в первой горизонтали одинаковые?"""
            matches_in_the_first_horizontal = 0
            matches_in_the_second_horizontal = 0
            matches_to_win = 3

            for stone in self.storage:
                if stone.color == stone_color:
                    if stone.index == 1 or stone.index == 5 or stone.index == 9:
                        matches_in_the_first_horizontal += 1
                    if stone.index == 3 or stone.index == 5 or stone.index == 7:
                        matches_in_the_second_horizontal += 1

            if matches_in_the_first_horizontal == matches_to_win \
                    or matches_in_the_second_horizontal == matches_to_win:
                return True
            return False

        return winning_rows(color) or winning_column(color) or victory_in_horizontal(color)

    def did_win_x(self):
        """проверяет выйграли ли крестики"""
        return self.is_win("x")

    def did_win_o(self):
        """проверяет выйграли лы нолики"""
        return self.is_win("0")

    def is_there_such_stone_on_board_according_to_index(self, cell_index: int):
        """проверяет есть ли такой камень на доске по его индексу"""
        for stone in self.storage:
            if stone.index == cell_index:
                return True
        return False

    def get_stone_by_index(self, cell_index):
        """возвращает камень с доски(не удаляет) по индексу"""
        for stone in self.storage:
            if stone.index == cell_index:
                return stone
        return False
