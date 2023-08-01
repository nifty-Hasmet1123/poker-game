from poker.validators import FlushValidator
from poker.card import Card
import unittest

class FlushValidatorTest(unittest.TestCase):
    def setUp(self):
        self.cards = [
            Card(rank = rank , suit = "Diamonds")
            for rank in ["2", "5", "8", "10", "Ace", "Jack"]
        ]

    def test_flush_validator(self):
        validator = FlushValidator(cards = self.cards)

        self.assertEqual(validator.is_valid(), True)

    # def test_flush_valid_cards(self):
    #     validator = FlushValidator(cards = self.cards)

    #     self.assertEqual(
    #         validator.valid_cards(),
    #         ["Diamonds"]
    #     )

    def test_flush_validator(self):
        validator = FlushValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                Card(rank = rank, suit = "Diamonds") 
                for rank in ["5", "8", "10", "Ace", "Jack"]
            ]
        )