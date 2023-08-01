from poker.card import Card
from poker.validators import FourOfAKindValidator
import unittest

class FourOfAKindValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.jack_of_hearts = Card(rank = "Jack", suit = "Hearts")
        self.jack_of_clubs = Card(rank = "Jack", suit = "Clubs")
        self.jack_of_diamonds = Card(rank = "Jack", suit = "Diamonds")
        self.jack_of_spades = Card(rank = "Jack", suit = "Spades")
        self.king_of_hearts = Card(rank = "King", suit = "Hearts")

        self.cards = [
            self.jack_of_hearts,
            self.jack_of_clubs,
            self.jack_of_diamonds,
            self.jack_of_spades,
            self.king_of_hearts,
            Card(rank = "Ace", suit = "Diamonds"),
            Card(rank = "4", suit = "Clubs")
        ]
    def test_four_of_a_kind_validator(self):
        validator = FourOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_valid_cards(self):
        validator = FourOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.jack_of_hearts,
                self.jack_of_clubs,
                self.jack_of_diamonds,
                self.jack_of_spades,
            ]
        )