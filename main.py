from player import Player_a
from game_deck import Deck
from player import Player_a


deck = Deck()
deck.shuffle()

dave = Player_a('Dave')
dave.draw(deck)
dave.show_hand()

