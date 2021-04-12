class Domino:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def show_tile(self, name):
        print(f'{name} - Domino : R {self.right} and L{self.left}')

