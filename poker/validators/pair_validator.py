from poker.validators import RankValidator

class PairValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Pair"

    def is_valid(self) -> bool:
        ranks_with_one_pair = self._ranks_with_count(2)
        return len(ranks_with_one_pair) == 1
    
    def valid_cards(self) -> list:
        ranks_with_pair = self._ranks_with_count(2) # dict
        pair_cards = [card for card in self.cards if card.rank in ranks_with_pair]

        return pair_cards 
    
        # pair_cards = list(filter(
        #     lambda card: card.rank in ranks_with_pair,
        #     sorted(self.cards, key = lambda card: card.suit) # sort card by card.suit
        # ))           