import random

class Card:

    def __init__(self):


        self.value = 0
        self.points = 300

    def card(self):

        self.value = random.randint(1,13)

        return self.value


class Game:

    def __init__(self):

        self.is_playing = True
        self.score = 0
        self.total_score = 300
        self.old_card = 0
        
        pass


    def start_game(self):
        
        while self.is_playing:
            self.player_guess()
            self.point_tally()
            self.output()



    def player_guess(self):
        
        card = Card()
        card.card()
    
        old_card = card.card()
        new_card = card.card()
        print(f'The card is: {old_card}')
        card_guess = input('Higher or lower? (h/l): ')
        print(f'Next card was: {new_card}')

        return card_guess

    def point_tally(self):

        if not self.is_playing:
            return

        # self.score = 100 if self.old_card > self.new_card and self.player_guess == 'h'else 100 if self.old_card < self.new_card and self.player_guess == 'l' else -75
        if self.old_card > self.new_card and self.player_guess == 'h':
            self.score = 100
        if self.old_card < self.new_card and self.player_guess == 'l':
            self.score = 100
        else:
            self.score = -75
        self.total_score += self.score
        
    def output(self):

        if not self.is_playing:
            return

        print(f'Your score is: {self.total_score}')
        again = input('Play again? (y/n): ')
        self.is_playing == (self.total_score > 0 and again == 'y')
