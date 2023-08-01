from poker.card import Card
from poker.validators import PairValidator
import unittest

class PairValidatorTest(unittest.TestCase):
    def test_pair_validator(self):
        cards = [
            Card(rank = "Ace", suit = "Clubs"),
            Card(rank = "Ace", suit = "Hearts")
        ]

        validator = PairValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_pair_from_card_collection(self):
        ten_of_spades = Card(rank = "10", suit = "Spades")
        ten_of_hearts = Card(rank = "10", suit = "Hearts")
        cards = [
            Card(rank = "Jack", suit = "Spades"),
            Card(rank = "2", suit = "Clubs"),
            Card(rank = "6", suit = "Diamonds"),
            ten_of_spades,
            ten_of_hearts,
        ]

        validator = PairValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [ten_of_spades, ten_of_hearts]
        )    