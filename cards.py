class Card:
    def __init__(self, suit, val,):
        self.suit = suit
        self.value = val
        

    def show(self, name):
        self.name = name
        print(f'{self.name} - Card   : The {self.value} of {self.suit}. ')
        

