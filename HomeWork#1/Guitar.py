class Guitar:
    def __init__(self, deck):
        self.deck = deck

    def suond_of_guitar(self):
        print(f'This guitar has {self.deck.deck_type}, and sounds good')


class Deck_type:
    def __init__(self, deck_type):
        self.deck_type = deck_type


deck = Deck_type('oak')
guitar = Guitar(deck)
guitar.suond_of_guitar()