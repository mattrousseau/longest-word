import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_word_is_valid(self):
        game = Game()
        game.grid = list("OQUWRBAZE")
        valid_word = "BAROQUE"
        self.assertTrue(game.is_valid(valid_word))
        self.assertEqual(game.grid, list('OQUWRBAZE'))

    def test_word_is_invalid(self):
        game = Game()
        game.grid = list("OQUWRBAZE")
        invalid_word = "TOTO"
        self.assertFalse(game.is_valid(invalid_word))
        self.assertEqual(game.grid, list('OQUWRBAZE'))

    def test_empty_word_is_invalid(self):
        game = Game()
        self.assertFalse(game.is_valid(""))

    def test_unknown_word_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KWIENFUQW')  # Forcer la grille à un scénario de test
        self.assertIs(new_game.is_valid('FEUN'), False)
