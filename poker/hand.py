from typing import Tuple, Union
from poker.validators import (
    RoyalFlushValidator,
    StraightFlushValidator,
    FourOfAKindValidator,
    FullHouseValidator,
    FlushValidator,
    StraightValidator,
    ThreeOfAKindValidator,
    TwoPairValidator,
    PairValidator, 
    HighCardValidator, 
    NoCardValidator
)

class Hand():
    VALIDATORS = (
        RoyalFlushValidator,
        StraightFlushValidator,
        FourOfAKindValidator,
        FullHouseValidator,
        FlushValidator,
        StraightValidator,
        ThreeOfAKindValidator,
        TwoPairValidator,
        PairValidator, 
        HighCardValidator, 
        NoCardValidator
    )

    def __init__(self):
        self.cards = []

    def __repr__(self):
        card_as_string = [str(card) for card in self.cards]

        return ", ".join(card_as_string)
    
    def add_cards(self, cards) -> None:
        copy_cards = self.cards[:]
        copy_cards.extend(cards)
        copy_cards.sort()

        self.cards = copy_cards
           
    def best_rank(self) -> Tuple[Union[int, str, list]]:
        for validator_klass in self.VALIDATORS:
            validator = validator_klass(cards = self.cards)
            
            if validator.is_valid():
                idx = self.VALIDATORS.index(validator_klass) # you can also use enumerate
                return (idx, validator.name, validator.valid_cards())