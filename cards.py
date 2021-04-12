class Card:
    def __init__(self, suit, val, card_value):
        self.suit = suit
        self.value = val
        self.card_value = card_value

    def show_card(self, name):
        print(f'{name} - Card  {self.card_value} : The {self.value} of {self.suit}. ')

# Score Value for the Card like 10 for King
        
        
