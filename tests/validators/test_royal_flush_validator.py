from poker.card import Card
from poker.validators import RoyalFlushValidator
import unittest

class RoyalFlushValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cards = [
            Card(rank = "2", suit = "Spades"),
            Card(rank = "10", suit = "Diamonds"),
            Card(rank = "Jack", suit = "Diamonds"),
            Card(rank = "Queen", suit = "Diamonds"),
            Card(rank = "King", suit = "Diamonds"),
            Card(rank = "Ace", suit = "Diamonds"),
            Card(rank = "Ace", suit = "Spades")

        ]

    def test_returns_five_straight_cards_with_the_same_rank_ending_in_ace(self):
        validator = RoyalFlushValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_valid_cards(self):
        validator = RoyalFlushValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                Card(rank = "10", suit = "Diamonds"),
                Card(rank = "Jack", suit = "Diamonds"),
                Card(rank = "Queen", suit = "Diamonds"),
                Card(rank = "King", suit = "Diamonds"),
                Card(rank = "Ace", suit = "Diamonds")
            ]
        )


