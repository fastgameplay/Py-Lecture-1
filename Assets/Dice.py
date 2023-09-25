import random

class Dice:
    def __init__(self, sides=6):
        self._validate(sides)
        self._sides = sides

    @staticmethod
    def _validate(sides):
        if sides < 2 or sides > 144:
            raise ValueError("Invalid number of sides for a dice. It should be between 2 and 144.")

    def roll(self):
        return random.randint(1, self._sides)