from poker.validators import FiveCardValidator

class StraightFlushValidator(FiveCardValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight Flush"

    @property
    def _straight_flush_card_batches(self) -> list:
        return [
            five_cards
            for five_cards in self._collection_of_five_straight_cards_in_a_row
            if len({card.suit for card in five_cards}) == 1
        ]

    def is_valid(self) -> bool:
        for five_cards in self._collection_of_five_straight_cards_in_a_row:
            unique_suits_in_next_five_cards = {card.suit for card in five_cards}

            if len(unique_suits_in_next_five_cards) == 1:
                return True
            
        return False
        
    def valid_cards(self) -> list:
        return self._straight_flush_card_batches[-1]