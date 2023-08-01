class NoCardValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "No cards"

    def is_valid(self) -> bool:
        return len(self.cards) == 0
    
    def valid_cards(self) -> list:
        return self.cards
        # or return []