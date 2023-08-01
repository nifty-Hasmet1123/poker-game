from .straight_flush_validator import StraightFlushValidator

class RoyalFlushValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "Royal Flush"

    @property
    def _straight_flush_validator(self):
        return StraightFlushValidator(self.cards)

    def is_valid(self):
        if self._straight_flush_validator.is_valid():
            straight_flush_cards = self._straight_flush_validator.valid_cards()
            is_royal = straight_flush_cards[-1].rank == "Ace"

            return is_royal
        return False
    
    def valid_cards(self):
        inclusion_cards = StraightFlushValidator(self.cards).valid_cards() # dict

        return list(filter(lambda card: card in inclusion_cards, self.cards))
        # cards = [card for card in self.cards if card in royal_flush_cards]
        # return cards