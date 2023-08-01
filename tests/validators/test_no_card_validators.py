from poker.validators import NoCardValidator
import unittest

class NoCardValidatorTest(unittest.TestCase):
    def test_validates_that_no_cards_are_present(self):
        validator = NoCardValidator(cards = [])

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_no_valid_cards(self):
        validator = NoCardValidator(cards = [])

        self.assertEqual(
            validator.valid_cards(),
            []
        )