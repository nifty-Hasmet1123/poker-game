from poker.validators import RankValidator

class FourOfAKindValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Four-of-a-kind"

    @property
    def _four_of_a_kind(self) -> dict:
        return self._ranks_with_count(4)
    
    def is_valid(self) -> bool:
        return len(self._four_of_a_kind) == 1
    
    def valid_cards(self) -> list[str]:
        return [card for card in self.cards if card.rank in self._four_of_a_kind]