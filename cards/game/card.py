import random

class Card:

    def __init__(self):


        self.value = 0
        self.points = 300

    def card(self):

        self.value = random.randint(1,13)

        return self.value
