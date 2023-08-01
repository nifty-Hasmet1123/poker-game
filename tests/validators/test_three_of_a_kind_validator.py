from poker.card import Card
from poker.validators import ThreeOfAKindValidator
import unittest

class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.king_of_diamonds = Card(rank = "King", suit = "Diamonds")
        self.king_of_hearts = Card(rank = "King", suit = "Hearts")
        self.king_of_spades = Card(rank = "King", suit = "Spades")
        
        self.cards = [
            Card(rank = "5", suit = "Hearts"),
            Card(rank = "8", suit = "Clubs"),
            self.king_of_diamonds,
            self.king_of_hearts,
            self.king_of_spades
        ]
            
    def test_three_of_a_kind_validator_is_valid(self):
        validator = ThreeOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )
    def test_returns_three_of_kind_card_from_collection(self):
        validator = ThreeOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.king_of_diamonds,
                self.king_of_hearts,
                self.king_of_spades
            ]
        )