from poker.card import Card
from poker.validators import TwoPairValidator
import unittest

class TwoPairValidatorTest(unittest.TestCase):
    def setUp(self): #
        """
        Remember to just put self on variables to make it
        available in the other function.
        And please don't use return here in setUp instance method!!!
        """

        self.ace_of_clubs = Card(rank = "Ace", suit = "Clubs")
        self.ace_of_diamonds = Card(rank = "Ace", suit = "Diamonds")
        self.ten_of_hearts = Card(rank = "10", suit = "Hearts")
        self.ten_of_spades = Card(rank = "10", suit = "Spades")

        self.cards = [
            Card(rank = "7", suit = "Clubs"),
            self.ace_of_clubs,
            self.ace_of_diamonds,
            self.ten_of_hearts, 
            self.ten_of_spades
        ]

    def test_two_pair_validator_test(self):
        validator = TwoPairValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_two_pair_from_card_collection(self):
        validator = TwoPairValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.ace_of_clubs, 
                self.ace_of_diamonds, 
                self.ten_of_hearts, 
                self.ten_of_spades
            ]
        )