from random import randint
from player import *
from cards import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for x_suit in ['Spades', 'Diamonds', 'Hearts', 'Clubs']:
            for y_value in range(1, 14):
                self.cards.append(Card(x_suit, y_value))

    def show(self):
        for a in self.cards:
            a.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = randint(0, i)
            self.cards[i], self.cards[r], = self.cards[r], self.cards[i]

    def draw_card(self):
        return self.cards.pop()

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self


