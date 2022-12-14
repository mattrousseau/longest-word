from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
        # setup
        game = Game()
        # exercise
        grid = game.grid
        # verify
        assert type(grid) ==list
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_uppercase

    def test_empty_word_is_invalid(self):
        game = Game()
        assert game.is_valid("") is False

    def test_is_valid(self):
        game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'EUREKA'
        game.grid = list(test_grid)

        assert game.is_valid(test_word) is True
        assert game.grid == list(test_grid)

    def test_is_invalid(self):
        game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'SANDWICH'
        game.grid = list(test_grid)
        assert game.is_valid(test_word) is False
        assert game.grid == list(test_grid)
