# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import string
import random

class Game():
    def __init__(self):
        self.grid = self.generate_grid()

    def generate_grid(self):
        return random.choices(string.ascii_uppercase, k=9)

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy()
        for letter in word:
            if letter not in letters:
                letters.remove(letter)
            else:
                return False
        return True
