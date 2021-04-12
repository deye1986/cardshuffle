from player import *
from game_deck import Deck
from dominoset import Dominopool as pool

def game_loop():
    
    deck = Deck()
    deck.shuffle()
    set_of_tiles = pool()
    set_of_tiles.shuffle_dominoes()

    player_one = 'Dave'
    player_two = 'Shadow'
    player_three = 'Dale'

    dave = Player(player_one)
    dave.draw(deck)
    dave.draw_domino(set_of_tiles)
    dave.show_hand(player_one)

    b = Player(player_two)
    b.draw(deck)
    b.draw_domino(set_of_tiles)
    b.show_hand(player_two)

    dale = Player(player_three)
    dale.draw(deck)
    dale.draw_domino(set_of_tiles)
    dale.show_hand(player_three)

game_loop()

