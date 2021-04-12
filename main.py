from player import Player_a
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

