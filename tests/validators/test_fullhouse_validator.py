from poker.card import Card
from poker.validators import FullHouseValidator
import unittest

class FullHouseValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.jack_of_hearts = Card(rank = "Jack", suit = "Hearts")
        self.jack_of_clubs = Card(rank = "Jack", suit = "Clubs")
        self.jack_of_diamonds = Card(rank = "Jack", suit = "Diamonds")
        self.king_of_spades = Card(rank = "King", suit = "Spades")
        self.king_of_hearts = Card(rank = "King", suit = "Hearts")

        self.cards = [
            self.jack_of_hearts,
            self.jack_of_clubs,
            self.jack_of_diamonds,
            Card(rank = "2", suit = "Diamonds"),
            self.king_of_spades,
            self.king_of_hearts,
            Card(rank = "4", suit = "Clubs"),
        ]

    def test_fullhouse_validator(self):
        validator = FullHouseValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_valid_cards(self):
        validator = FullHouseValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.jack_of_clubs,
                self.jack_of_diamonds,
                self.jack_of_hearts,
                self.king_of_hearts,
                self.king_of_spades,
            ]
        )