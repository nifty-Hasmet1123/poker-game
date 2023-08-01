from .three_of_a_kind_validator import ThreeOfAKindValidator
from .pair_validator import PairValidator

class FullHouseValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "FullHouse"

    def is_valid(self) -> bool:
        return (
            ThreeOfAKindValidator(self.cards).is_valid() and
            PairValidator(self.cards).is_valid()
        )
    
    def valid_cards(self) -> list[str]:
        three_of_a_kind = ThreeOfAKindValidator(self.cards).valid_cards()
        pair = PairValidator(self.cards).valid_cards()

        return sorted(three_of_a_kind + pair)
    
# from poker.validators import ThreeOfAKindValidator, PairValidator
# this doesn't work because the ThreeOfAKindValidator and PairValidator
# is partially initialize only. you need to put this on the upper
# line in the __init__.py for this to work.