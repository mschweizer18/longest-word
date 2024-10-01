import random
import string
import requests

# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = [] # TODO

        for i in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))


    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if not word:
            return False

        response = requests.get(f'https://dictionary.lewagon.com/{word}').json()

        grid = self.grid.copy()
        for letter in word:
            if letter in grid and response['found'] == True:
                grid.remove(letter)
            else:
                return False
            return True
