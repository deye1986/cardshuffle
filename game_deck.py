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
                for card_value in range(1, 14):
                    if y_value == 1:
                        card_value = 'Ace'
                        self.cards.append(Card(x_suit, y_value, card_value=card_value))
                    elif y_value == 11:
                        card_value = 'Jack'
                        self.cards.append(Card(x_suit, y_value, card_value=card_value))
                    elif y_value == 12:
                        card_value = 'Queen'
                        self.cards.append(Card(x_suit, y_value, card_value=card_value))
                    elif y_value == 13:
                        card_value = 'King'
                        self.cards.append(Card(x_suit, y_value, card_value=card_value))
                    else:
                        card_value = None
                        self.cards.append(Card(x_suit, y_value, card_value=card_value))


    def show_card(self):
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


