from random import randint
from domino import Domino


class Dominopool:
    def __init__(self):
        self.set = []
        self.buildset()

    def buildset(self):
        for l_side in range(0, 6):
            for r_side in range(0, 6):
                self.set.append(Domino(l_side, r_side))

    def show(self):
        for b in self.set:
            b.show()

    def shuffle_dominoes(self):
        for i in range(len(self.set) - 1, 0, -1):
            r = randint(0, i)
            self.set[i], self.set[r], = self.set[r], self.set[i]

    def draw_tile(self):
        return self.set.pop()

    def draw(self, pool):
        self.hand.append(pool.draw_tile())
        return self
        
        