class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        
    def show_card(self, name):
        print(f'{name} - Card   : The {self.value} of {self.suit}. ')
        
