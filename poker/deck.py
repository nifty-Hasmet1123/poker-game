import random

class Deck():
    def __init__(self):
        self._cards = [] # put this on a protected attribute.
    
    def __len__(self):
        return len(self._cards)

    def add_cards(self, cards) -> None:
        self._cards.extend(cards)
    
    def remove_cards(self, count) -> None:
        cards_to_remove = self._cards[:count]
        del self._cards[:count]

        return cards_to_remove

    def shuffle_cards(self) -> None:
        random.shuffle(self._cards)    