# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import string
import random
import requests

class Game():
    def __init__(self):
        self.generate_random_grid()

    def generate_random_grid(self):
        self.grid = random.choices(string.ascii_uppercase, k=9)

    def is_valid(self, word):
        if not word:
            return False
        grid_copy = self.grid.copy()
        word_letters = list(word)
        for word_letter in word_letters:
            if word_letter in grid_copy:
                grid_copy.remove(word_letter)
            else:
                return False
        return self.__check_dictionary(word)

    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f'https://wagon-dictionary.herokuapp.com/{word}').json()
        return response['found']
