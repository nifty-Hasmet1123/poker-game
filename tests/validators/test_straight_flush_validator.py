from poker.card import Card
from poker.validators import StraightFlushValidator
import unittest

class StraightFlushValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cards = [
            Card(rank = rank, suit = "Diamonds")
            for rank in ["6", "7", "8", "9", "10"]
        ]

        self.copy = self.cards[:]
        self.copy.extend([
            Card(rank = "Jack", suit = "Diamonds"),
            Card(rank = "King", suit = "Clubs")
        ])

    def test_straight_flush_validator_is_valid(self):
        validator = StraightFlushValidator(cards = self.copy)

        self.assertEqual(
            validator.is_valid(),
            True
        )
    
    def test_valid_cards(self):
        validator = StraightFlushValidator(cards = self.copy)
        expected_valid_cards = self.copy[1:6]

        self.assertEqual(
            validator.valid_cards(),
            expected_valid_cards
        )