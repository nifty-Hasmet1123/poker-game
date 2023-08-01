class HighCardValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "High Card"

    def is_valid(self) -> bool:
        return len(self.cards) >= 2
    
    def valid_cards(self) -> list:
        return self.cards[-1:]