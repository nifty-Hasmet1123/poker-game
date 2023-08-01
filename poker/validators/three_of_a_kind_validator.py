from poker.validators import RankValidator

class ThreeOfAKindValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Three of a kind"
    
    def is_valid(self) -> bool:
        ranks_with_three_of_a_kind = self._ranks_with_count(3)
        return len(ranks_with_three_of_a_kind) >= 1
    
    def valid_cards(self) -> list:
        ranks_with_three_of_a_kind = self._ranks_with_count(3)

        filt = list(filter(
            lambda card: card.rank in ranks_with_three_of_a_kind,
            self.cards
        ))

        return filt