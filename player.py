class Player_a:
    def __init__(self, name):
        self.name = (name)
        self.hand = []
        self.tiles = [] # dominos 

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def draw_domino(self, domino_hand):
        self.tiles.append(domino_hand.draw_tile())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show()
        for domino in self.tiles:
            domino.show_tile()

