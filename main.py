from player import *
from game_deck import Deck
from dominoset import Dominopool


deck = Deck()
deck.shuffle()
set_of_tiles = Dominopool()
set_of_tiles.shuffle_dominoes()


dave = Player_a('Dave')
dave.draw(deck)
dave.draw_domino(set_of_tiles)
dave.show_hand()

shadow = Player_b('Shadow')
shadow.draw(deck)
shadow.draw_domino(set_of_tiles)
shadow.show_hand()

