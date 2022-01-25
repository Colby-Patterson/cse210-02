from game.card import Card

class Game:

    def __init__(self):

        self.is_playing = True
        self.score = 0
        self.total_score = 300
        self.old_card = 0
        self.new_card = 0
        
        pass


    def start_game(self):
        
        while self.is_playing:
            self.player_guess()
            self.point_tally()
            self.output()



    def player_guess(self):

        if not self.is_playing:
            return
        
        card = Card()
    
        self.old_card = card.card()
        self.new_card = card.card()
        print(f'The card is: {self.old_card}')
        self.card_guess = input('Higher or lower? (h/l): ')
        print(f'Next card was: {self.new_card}')

        return self.card_guess

    def point_tally(self):

        if not self.is_playing:
            return

        self.score = 100 if self.old_card > self.new_card and self.card_guess == 'l'else 100 if self.old_card < self.new_card and self.card_guess == 'h' else -75
        #if self.old_card > self.new_card and self.card_guess == 'l':
            #self.score = 100
        #if self.old_card < self.new_card and self.card_guess == 'h':
            #self.score = 100
        #else:
            #self.score = -75
        self.total_score += self.score

        return self.total_score
        
    def output(self):

        if not self.is_playing:
            return

        print(f'Your score is: {self.total_score}')
        again = input('Play again? (y/n): ')
        if self.total_score > 0 and again == 'y':
            self.is_playing = True
        else:
            self.is_playing = False