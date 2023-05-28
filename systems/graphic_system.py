from painter.painter import Painter
import time


class GraphicSystem:
    """отвечает за отрисовку"""

    def __init__(self):
        self.painter = Painter(40, 20)

    def display_game_rules(self):
        """просто выводит на экрна start game и название игры"""
        self.painter.clear()
        self.painter.add_picture("Tic Tac Toe", 14, 8)
        self.painter.add_picture("start game", 15, 10)
        self.painter.display()
        time.sleep(1)

    def create_main_screen(self, field: str, step: str, whose_move: str):
        """создает главный экран с игровым полем"""
        self.painter.add_picture("Tic Tac Toe", 13, 4)
        self.painter.add_picture(f"It's a move now:{whose_move}", 5, 6)
        self.add_game_field(field)
        self.add_example_of_field_with_hints()
        self.painter.add_picture(f"step counter:{step}", 5, 15)

    def display_main_screen(self, field: str, step: str, whose_move: str):
        """воспроизводит главный игран"""
        self.painter.clear()
        self.create_main_screen(field, step, whose_move)
        self.painter.display()

    def create_display_error(self, field: str, step: str, massage: str, whose_move: str):
        """создает главный экрна с добавление ошибки игрока"""
        self.create_main_screen(field, step, whose_move)
        self.create_error_message(massage)

    def display_error_screen(self, field: str, step: str, massage: str, whose_move: str):
        """воспроизводит экран с ошибкой игрока"""
        self.painter.clear()
        self.create_display_error(field, step, massage, whose_move)
        self.painter.display()
        time.sleep(2)

    def add_example_of_field_with_hints(self):
        """добавляет на эран игровое поле с подсказками индексов ячеек"""
        example = """[1] [2] [3]\n[4] [5] [6]\n[7] [8] [9]"""
        self.painter.add_picture("Hints:", 22, 8)
        self.painter.add_picture(example, 20, 10)

    def add_game_field(self, field):
        """добавляет игровое поле на экран"""
        self.painter.add_picture("Game Field:", 5, 8)
        self.painter.add_picture(field, 5, 10)

    def create_error_message(self, massage):
        """создает окно ошибки"""
        self.painter.add_picture("************************", 2, 17)
        self.painter.add_picture(massage, 5, 18)
        self.painter.add_picture("************************", 2, 19)
        self.painter.add_picture("*", 25, 18)

    def create_winner_screen(self, whose_win: str, step: str, game_field: str):
        """создает экран победителя"""
        sample = """
         \\  /\\  /  0   |\\ |
          \\/  \\/   |   | \\|
         """
        self.painter.add_picture(sample, 2, 10)
        self.painter.add_picture(f"The player playing for the {whose_win} won", 5, 8)
        self.painter.add_picture(f"Number of moves:{step}", 5, 6)
        self.painter.add_picture("Tic Tac Toe", 13, 4)
        self.painter.add_picture("Game field:", 5, 14)
        self.painter.add_picture(game_field, 10, 16)

    def display_winner_screen(self, whose_win: str, step: str, game_field: str):
        """воспроизводит экран победителя"""
        self.painter.clear()
        self.create_winner_screen(whose_win, step, game_field)
        self.painter.display()

    def create_screen_no_one_has_won(self, step: str, game_field):
        """создает экрна ничьей"""
        sample = """
         |  |--  / \\  \\  /\\  /
        0|  |   / --\\  \\/  \\/   
        """
        self.painter.add_picture("Tic Tac Toe", 13, 6)
        self.painter.add_picture(f"Number of moves:{step}", 10, 8)
        self.painter.add_picture(sample, 3, 9)
        self.painter.add_picture("Game field:", 5, 14)
        self.painter.add_picture(game_field, 10, 16)

    def display_screen_no_one_has_won(self, step: str, game_field: str):
        """воспроизводит экран ничьей"""
        self.painter.clear()
        self.create_screen_no_one_has_won(step, game_field)
        self.painter.display()
