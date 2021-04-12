class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print(f'Card   : The {self.value} of {self.suit}. ')
        

