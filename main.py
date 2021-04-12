from player import *
from game_deck import Deck
from dominoset import Dominopool

def game_loop():
    deck = Deck()
    deck.shuffle()
    set_of_tiles = Dominopool()
    set_of_tiles.shuffle_dominoes()

    player_one = 'Dave'
    player_two = 'Shadow'

    dave = Player(player_one)
    dave.draw(deck)
    dave.draw_domino(set_of_tiles)
    dave.show_hand(player_one)

    shadow = Player(player_two)
    shadow.draw(deck)
    shadow.draw_domino(set_of_tiles)
    shadow.show_hand(player_two)

game_loop()

