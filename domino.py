class Domino:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def show_tile(self, name):
        print(f'{name} - Tile : R{self.right} and {self.left} element.')

