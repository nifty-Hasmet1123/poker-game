from poker.validators import FiveCardValidator

class StraightValidator(FiveCardValidator):   
    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight"

    def is_valid(self) -> bool:
        return len(self._collection_of_five_straight_cards_in_a_row) >= 1
        
    def valid_cards(self) -> list:
        return self._collection_of_five_straight_cards_in_a_row[-1] 
        # returns last index of list