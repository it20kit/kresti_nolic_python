from systems.keyboard import Keyboard
from game_objects.board import Board
from game_objects.stone import Stone


class GameManager:
    """управляет логикой игры"""

    def __init__(self):
        self.__step = 0
        self.keyboard = Keyboard()
        self.board = Board()
        self.__player_input = None

    def update_game_state(self):
        """ставит камень на доску"""
        self.board.add_stone_stone_board(self.create_stone())

    def get_input_from_player(self, massage):
        """принемает ввод от игрока"""
        return self.keyboard.input_plyer(massage)

    def clear_player_input(self):
        """очищает ввод игрока"""
        self.__player_input = None

    def add_player_input(self, player_input: str):
        """сохраняет ввод игрока"""
        self.__player_input = player_input

    def check_player_input(self):
        """проверяет ввод игрока(игрок должен вводить число, а не строки)"""
        try:
            if self.entered_data_acceptable():
                raise Exception("Invalid input")
        except ValueError:
            raise Exception('Input error')

    def entered_data_acceptable(self):
        """проверяет чтобы введеные данные были не больше 9 и не меньше 1"""
        return int(self.__player_input) > 9 or int(self.__player_input) < 1

    def increment_step_counter(self):
        """увеличивает счетчик ходов на еденицу"""
        self.__step += 1

    def determine_whose_move(self):
        """определяет чей ход сейчас, и возвращает цвет камня"""
        if self.__step % 2 == 0:
            return "x"
        return "0"

    def create_stone(self):
        """создает камень по собранным параметрам"""
        color = self.determine_whose_move()
        cell_index = int(self.__player_input)
        return Stone(color, cell_index)

    def is_it_possible_to_make_such_move(self):
        """проверяет можно ли сделать такой ход"""
        if self.board.is_there_such_stone_on_board_according_to_index(int(self.__player_input)):
            raise Exception('Cell not free')

    def is_there_winner(self):
        """проверяет есть ли победитель"""
        return self.board.did_win_x() or self.board.did_win_o()

    def this_is_draw(self):
        """проверяет ничью"""
        return self.__step == 9

    @property
    def step(self):
        return self.__step

    @step.setter
    def step(self, step: int):
        self.__step = step
