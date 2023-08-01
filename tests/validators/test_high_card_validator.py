# if without an __init__ file inside the poker.validators you need this command.
# from poker.validators.high_card_validator import HighCardValidator
from poker.card import Card
from poker.validators import HighCardValidator 
# you need to add a import inside the poker validator folder.
# from .high_card_validator import HighCardValidator
import unittest

class HighCardValidatorTest(unittest.TestCase):
    def test_validates_if_card_have_a_high_card(self):
        cards = [
            Card(rank = "8", suit = "Clubs"),
            Card(rank = "Queen", suit = "Spades")
        ]

        validator = HighCardValidator(cards = cards)
        
        self.assertEqual(validator.is_valid(), True)

    def test_returns_high_card_from_card_collection(self):
        ace_of_spades = Card(rank = "Ace", suit = "Spades")

        cards = [
            Card(rank = "8", suit = "Spades"),
            Card(rank = "9", suit = "Hearts"),
            Card(rank = "2", suit = "Clubs"),
            Card(rank = "Jack", suit = "Hearts"),
            ace_of_spades
        ]

        validator = HighCardValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [ace_of_spades]
        )