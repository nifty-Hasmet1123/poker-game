from poker.validators import RankValidator

class TwoPairValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Two Pair"
     
    def is_valid(self) -> bool:
        ranks_with_two_pair = self._ranks_with_count(2)
        return len(ranks_with_two_pair) == 2
    
    def valid_cards(self) -> list:
        ranks_with_two_pair = self._ranks_with_count(2) # {key:value}
        
        two_pair_cards = list(filter(
            lambda card: card.rank in ranks_with_two_pair, # no need to use keys()
            self.cards
        ))

        return two_pair_cards


