import random

class Deck:
    def __init__(self):
        self.cards = [ 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8 ]
        return random.shuffle(self.cards)
        
    def draw(self):
        if len(self.cards) == 0:
            raise ValueError("Empty Deck...")
        return self.cards.pop()
    
    def remaining_cards(self):
        return len(self.cards)