from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
        new_game = Game()

        grid = new_game.grid

        assert isinstance(grid, list)
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_uppercase

    def test_empty_word_is_invalid(self):
        # setup
        new_game = Game()
        # verify
        assert new_game.is_valid('') is False

    def test_is_valid(self):
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'EUREKA'

        new_game.grid = list(test_grid)

        assert new_game.is_valid(test_word) is True
        assert new_game.grid == list(test_grid)

    def test_is_invalid(self):
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'SANDWICH'

        new_game.grid = list(test_grid)

        assert new_game.is_valid(test_word) is False
        assert new_game.grid == list(test_grid)
