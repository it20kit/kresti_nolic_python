from systems.graphic_system import GraphicSystem
from systems.game_manager import GameManager


class Game:
    """реализует цикл игры"""

    def __init__(self):
        self.running = True
        self.graphic_system = GraphicSystem()
        self.game_manager = GameManager()

    def run(self):
        """цикл игры"""
        self.graphic_system.display_game_rules()
        while self.running:
            try:
                self.graphic_system.display_main_screen(
                    self.game_manager.board.to_string(),
                    self.game_manager.step,
                    self.game_manager.determine_whose_move()
                )
                self.game_manager.add_player_input(self.game_manager.get_input_from_player("enter cell index:"))
                self.game_manager.check_player_input()
                self.game_manager.is_it_possible_to_make_such_move()
                self.game_manager.update_game_state()
                self.game_manager.clear_player_input()
                if self.game_manager.is_there_winner():
                    self.graphic_system.display_winner_screen(
                        self.game_manager.determine_whose_move(),
                        self.game_manager.step,
                        self.game_manager.board.to_string()
                    )
                    self.running = False
                self.game_manager.increment_step_counter()
                if self.game_manager.this_is_draw():
                    self.graphic_system.display_screen_no_one_has_won(
                        self.game_manager.step,
                        self.game_manager.board.to_string()
                    )
                    self.running = False
            except Exception as error:
                self.graphic_system.display_error_screen(
                    self.game_manager.board.to_string(),
                    self.game_manager.step,
                    str(error), self.game_manager.determine_whose_move())
