import random
import string

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

        grid = self.grid.copy()
        for letter in word:
            if letter in grid:
                grid.remove(letter)
            else:
                return False
            return True
